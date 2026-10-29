# ✍️ InkGenius AI — Handwritten Digit Recognition

InkGenius AI is a web-based handwritten digit recognition application built with Python, TensorFlow, and Flask. Users can draw a digit from **0 to 9** on a digital canvas and receive a prediction from a trained machine learning model.

## 🚀 Features

* 🎨 Interactive drawing canvas for handwritten digits.
* 🤖 Machine learning model trained on the MNIST dataset.
* 🔢 Predicts handwritten digits from 0 to 9.
* 📊 Displays prediction results and confidence information.
* 🧹 Clear the canvas and try another digit.
* 🌐 Simple web interface powered by Flask.
* 📈 Reported MNIST test accuracy: **97.23%**.

## 🛠️ Technologies Used

* **Python** — application logic and model integration.
* **TensorFlow / Keras** — machine learning model.
* **Flask** — web application framework.
* **NumPy** — numerical processing.
* **Pillow** — image processing.
* **HTML, CSS, and JavaScript** — web interface and drawing canvas.

## 📁 Project Structure

```text
HandwrittenCharacterRecognition/
├── app.py
├── train_model.py
├── predict_digit.py
├── preprocess.py
├── inkgenius_model.keras
├── requirements.txt
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/joyceolive-26/CodeAlpha_InkGeniusAI.git
```

### 2. Open the project folder

```bash
cd CodeAlpha_InkGeniusAI
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open this address in your browser:

```text
http://127.0.0.1:5000
```

## 🧠 Model Information

The application uses a trained neural network for handwritten digit classification using the MNIST dataset.

* **Task:** Digit classification.
* **Input:** A handwritten digit drawn on the canvas.
* **Output:** Predicted digit from 0 to 9.
* **Reported test accuracy:** 97.23%.

Actual predictions may vary depending on handwriting style and image preprocessing.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Building a machine learning application.
* Integrating a trained model with a Flask web application.
* Processing images before prediction.
* Creating an interactive browser-based interface.
* Organizing Python project files and dependencies.
* Using Git and GitHub for version control and project sharing.

## 🔮 Future Improvements

* Add support for recognizing handwritten letters.
* Improve preprocessing for different handwriting styles.
* Display a ranked list of prediction probabilities.
* Deploy the application online.
* Add screenshots and a demonstration video.

## 👩‍💻 Author

**Joyce Olive**

GitHub: [joyceolive-26](https://github.com/joyceolive-26)

## 📄 License

This project is intended for educational and portfolio purposes.
