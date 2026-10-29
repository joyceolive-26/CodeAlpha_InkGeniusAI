
import os
import base64
from io import BytesIO

import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request, jsonify
from PIL import Image, UnidentifiedImageError

# Create Flask application
app = Flask(__name__)

# Load the trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "inkgenius_model.keras")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = tf.keras.models.load_model(MODEL_PATH)


# Display the website
@app.route("/")
def home():
    return render_template("index.html")


# Predict a handwritten digit
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)

        if not data or not data.get("image"):
            return jsonify({
                "error": "No drawing received. Please draw a digit."
            }), 400

        image_data = data["image"]

        # Remove the data URL prefix
        if "," in image_data:
            image_data = image_data.split(",", 1)[1]

        # Decode the uploaded image
        image_bytes = base64.b64decode(image_data, validate=True)

        with Image.open(BytesIO(image_bytes)) as source:
            image = source.convert("L")

        image_array = np.array(image)

        # Locate the white strokes
        foreground = image_array > 30

        if not np.any(foreground):
            return jsonify({
                "error": "Please draw a digit before predicting."
            }), 400

        # Find the digit boundaries
        rows = np.where(np.any(foreground, axis=1))[0]
        cols = np.where(np.any(foreground, axis=0))[0]

        top = int(rows[0])
        bottom = int(rows[-1] + 1)
        left = int(cols[0])
        right = int(cols[-1] + 1)

        # Crop the digit
        cropped = image.crop((left, top, right, bottom))

        # Resize proportionally to fit within 20 x 20
        cropped.thumbnail((20, 20), Image.Resampling.LANCZOS)

        # Center the digit on a 28 x 28 black canvas
        canvas = Image.new("L", (28, 28), 0)

        x_offset = (28 - cropped.width) // 2
        y_offset = (28 - cropped.height) // 2

        canvas.paste(cropped, (x_offset, y_offset))

        # DEBUG: Save a larger preview of the image sent to the model
        preview = canvas.resize(
            (280, 280),
            Image.Resampling.NEAREST
        )

        preview_path = os.path.join(
            BASE_DIR, "debug_processed.png"
        )
        preview.save(preview_path)

        print("Processed image saved to:", preview_path)

        # Normalize pixels from 0-255 to 0-1
        image_array = np.array(
            canvas, dtype=np.float32
        ) / 255.0

        # Match the model's input shape
        if len(model.input_shape) == 4:
            image_array = image_array.reshape(1, 28, 28, 1)
        elif len(model.input_shape) == 3:
            image_array = image_array.reshape(1, 28, 28)
        else:
            return jsonify({
                "error": "Unsupported model input shape."
            }), 500

        # Predict the digit
        predictions = model.predict(
            image_array, verbose=0
        )[0]

        # Print all ten digit scores for debugging
        print(
            "Digit probabilities (0-9):",
            np.round(predictions * 100, 2)
        )

        # Select the three highest scores
        top_three = np.argsort(predictions)[-3:][::-1]

        results = []

        for digit_index in top_three:
            results.append({
                "digit": int(digit_index),
                "confidence": round(
                    float(predictions[digit_index]) * 100, 2
                )
            })

        # Main prediction
        digit = results[0]["digit"]
        confidence = results[0]["confidence"]

        return jsonify({
            "digit": digit,
            "confidence": confidence,
            "top_three": results
        })

    except (
        ValueError,
        TypeError,
        UnidentifiedImageError
    ) as error:
        app.logger.warning("Invalid drawing image: %s", error)

        return jsonify({
            "error": "Could not process the drawing. Please try again."
        }), 400

    except Exception:
        app.logger.exception("Prediction failed")

        return jsonify({
            "error": "Prediction failed. Check the terminal."
        }), 500


# Start Flask
if __name__ == "__main__":
    app.run(debug=True)

