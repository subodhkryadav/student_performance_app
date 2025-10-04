from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# =========================
# Load the ML model
# =========================
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'Student_Performance_model.pickle')

try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print(f"✅ Model loaded successfully from: {MODEL_PATH}")
except Exception as e:
    model = None
    print(f"⚠️ Warning: could not load model at {MODEL_PATH}: {e}")


# =========================
# Routes
# =========================
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Place Student_Performance_model.pickle in project root.'}), 500

    try:
        # Read input features from JSON
        data = request.json or {}
        # Expected keys: hours_studied, previous_scores, sleep_hours, sample_papers
        hs = float(data.get('hours_studied', 0))
        ps = float(data.get('previous_scores', 0))
        sh = float(data.get('sleep_hours', 0))
        sp = float(data.get('sample_papers', 0))

        X = np.array([[hs, ps, sh, sp]])

        # =========================
        # Prediction
        # =========================
        try:
            # Regression prediction
            y_pred = model.predict(X)
            perf = float(y_pred[0])
            perf = round(perf, 2)
            result = {
                'performance_index': perf,
                'message': 'Predicted Performance Index (numeric).'
            }
        except Exception:
            # Fallback: classification probability
            try:
                proba = model.predict_proba(X)
                p = float(np.max(proba) * 100)
                result = {
                    'performance_index': round(p, 2),
                    'message': 'Predicted probability-based Performance Index (0-100).'
                }
            except Exception as e:
                return jsonify({'error': f'Prediction failed: {e}'}), 500

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': f'Invalid input or server error: {e}'}), 400


# =========================
# Run the app
# =========================
if __name__ == '__main__':
    # Use PORT from environment (for Koyeb/PA), default 5000 for local dev
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
