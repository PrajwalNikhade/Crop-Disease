"""
Prediction Module — Crop Disease Detection
"""

import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "crop_disease_model.h5")
CLASS_NAMES_PATH = os.path.join(BASE_DIR, "models", "class_names.json")

IMG_SIZE = 128

_model = None
_class_names = None


def get_model():
    """Load model (cached)."""
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model not found at {MODEL_PATH}. "
                "Please train the model first using scripts/train_model.py"
            )
        _model = load_model(MODEL_PATH)
    return _model


def get_class_names():
    """Load class names mapping (cached)."""
    global _class_names
    if _class_names is None:
        if not os.path.exists(CLASS_NAMES_PATH):
            raise FileNotFoundError(
                f"Class names not found at {CLASS_NAMES_PATH}. "
                "Please train the model first."
            )
        with open(CLASS_NAMES_PATH, "r") as f:
            _class_names = json.load(f)
    return _class_names


def predict_disease(img_file):
    """
    Predict disease from an uploaded image file.

    Args:
        img_file: File-like object or path to image

    Returns:
        dict with keys: class_name, confidence, all_predictions
    """
    model = get_model()
    class_names = get_class_names()

    # Load and preprocess image
    img = image.load_img(img_file, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Predict
    predictions = model.predict(img_array, verbose=0)
    predicted_index = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_index]) * 100

    class_name = class_names[str(predicted_index)]

    return {
        "class_name": class_name,
        "confidence": round(confidence, 2),
        "all_predictions": predictions[0]
    }


def is_model_available():
    """Check if trained model exists."""
    return os.path.exists(MODEL_PATH) and os.path.exists(CLASS_NAMES_PATH)
