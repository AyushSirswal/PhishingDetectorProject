
# Phishing URL & Email Detector

This project provides a web-based application that detects phishing URLs and emails using machine learning models. The app allows users to input a URL or email content and determine whether it's benign or potentially malicious.

## Features

- **URL Phishing Detection**: Identifies whether a given URL is benign or malicious.

## Technologies Used

- **Python** (Flask for backend)
- **Machine Learning** (Scikit-learn for phishing detection models)
- **HTML, CSS, JavaScript** for the frontend
- **TF-IDF** for feature extraction
- **Joblib** to load pre-trained models

## Setup

### Prerequisites

Make sure you have Python installed (preferably Python 3.x). You will also need to install the following Python packages:

- Flask
- joblib
- scikit-learn
- numpy
- regex (re)

You can install these dependencies using pip:

```bash
pip install flask joblib scikit-learn numpy
```

### Project Structure

```
PhishingDetection/
├── app.py                # Main Flask application
├── model_url.pkl         # Pre-trained URL phishing model
├── templates/
│   └── index.html        # Frontend HTML for the web application
└── static/
    └── style.css         # Custom CSS for styling the app
    └── script.js         # JavaScript for interactivity
```

### Running the Application

1. **Start the Flask app**:
   - Navigate to the project directory and run the following command to start the Flask server:

   ```bash
   python app.py
   ```

   - The app will be available at `http://127.0.0.1:5000/`.

2. **Access the App**:
   - Open your browser and go to `http://127.0.0.1:5000/` to access the phishing URL and email detector.

### Scanning URLs

- On the main page, enter a URL into the input field and click "Scan URL".
- The app will display whether the URL is benign or malicious based on the trained machine learning model.


## Models Used

### URL Phishing Detection Model

- **Model**: A pre-trained machine learning model that predicts whether a URL is phishing or benign based on extracted features like length, number of digits, special characters, subdomains, and suspicious words.


## How URL Detection Works

1. **Feature Extraction**:
   The system extracts features from the given URL, including:
   - URL length
   - Number of digits
   - Number of special characters
   - Number of subdomains
   - Presence of HTTPS
   - Presence of suspicious words like "login," "secure," "bank," etc.
   
2. **Model Prediction**:
   The extracted features are fed into a pre-trained model, which classifies the URL as either **benign** or **malicious** based on the learned patterns.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
#   P h i s h i n g D e t e c t o r P r o j e c t  
 