from flask import Flask, request, jsonify, render_template
import joblib
import re
import os
import numpy as np

# Load trained models
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_url = joblib.load(os.path.join(BASE_DIR, 'model_url.pkl'))

# Flask app
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Route for the homepage to serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# Feature extraction for URL phishing detection
def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['num_digits'] = sum(c.isdigit() for c in url)
    features['num_special_chars'] = len(re.findall(r'\W', url))
    features['num_subdomains'] = url.count('.') - 1
    features['has_https'] = int('https' in url)
    features['has_ip'] = int(bool(re.search(r'(\d{1,3}\.){3}\d{1,3}', url)))
    features['has_at_symbol'] = int('@' in url)
    features['has_dash'] = int('-' in url)
    features['has_suspicious_word'] = int(any(word in url for word in ['login', 'secure', 'bank', 'update', 'verify']))
    return features

# Route for URL phishing detection
@app.route('/url_scan', methods=['POST'])
def url_scan():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Extract features from the URL
    features = extract_features(url)
    
    # Convert features to a numpy array
    X_url = np.array(list(features.values())).reshape(1, -1)
    
    # Predict using the URL model
    prediction = model_url.predict(X_url)
    
    result = 'malicious' if prediction[0] == 1 else 'benign'
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
