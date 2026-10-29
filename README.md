
# InkGenius AI — Handwritten Digit Recognition

InkGenius AI is a web application that recognizes handwritten digits from 0 to 9 using a neural network trained on the MNIST dataset.

Users can draw digits on a canvas and view the predicted digit, confidence score, top three predictions, and recent prediction history.

## Features

- Interactive drawing canvas
- Handwritten digit recognition
- Top 3 predictions with confidence percentages
- Visual confidence bars
- Recent prediction history
- Clear canvas and clear history options
- Image cropping, resizing, and normalization
- Flask web application powered by TensorFlow

## Technologies Used

- Python
- TensorFlow and Keras
- NumPy
- Pillow
- Flask
- HTML
- CSS
- JavaScript
- MNIST dataset

## Model Performance

The trained model achieved 97.23% accuracy on the MNIST test dataset in my training run.

This is the model's accuracy on the MNIST test set. Results may differ when recognizing handwritten digits drawn by users.

## Project Structure

```text
HandwrittenCharacterRecognition/
├── app.py
├── train_model.py
├── predict_digit.py
├── preprocess.py
├── inkgenius_model.keras
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## Requirements

- Python 3.12 recommended
- pip
- The trained model file: `inkgenius_model.keras`

## Run the Project Locally

### 1. Get the project files

Clone or download this repository and open a terminal inside the project folder.

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
```

### 3. Install dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Start the application

```powershell
.\.venv\Scripts\python.exe app.py
```

### 5. Open the website

Visit:

http://127.0.0.1:5000

## How to Use

1. Open the website.
2. Draw a digit from 0 to 9.
3. Click **Predict Digit**.
4. View the main prediction and top three predictions.
5. Use **Clear Canvas** to draw another digit.
6. View or clear your prediction history.

## Future Improvements

- Improve recognition across different handwriting styles
- Add automated tests
- Save history across browser sessions
- Add a confusion matrix and detailed model evaluation
- Deploy the application for public access

## Author

Developed as a personal AI and software development learning project.
