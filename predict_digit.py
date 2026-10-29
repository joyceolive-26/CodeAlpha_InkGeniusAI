
import tensorflow as tf
import numpy as np

# Load the saved model
model = tf.keras.models.load_model("inkgenius_model.keras")

# Load the MNIST test dataset
(_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Select one test image
image = x_test[0]
actual_digit = y_test[0]

# Prepare the image
image = image.astype("float32") / 255.0
image = np.expand_dims(image, axis=0)

# Predict the digit
predictions = model.predict(image, verbose=0)[0]

# Find the top 3 predictions
top_three = np.argsort(predictions)[-3:][::-1]

print("Actual digit:", actual_digit)
print("\nTop 3 predictions:")

for digit in top_three:
    confidence = float(predictions[digit]) * 100
    print(f"Digit: {digit}, Confidence: {confidence:.2f}%")
