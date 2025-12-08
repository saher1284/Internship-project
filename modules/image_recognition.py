import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, decode_predictions
from modules.image_processing import preprocess_image

model = MobileNetV2(weights="imagenet")

def identify_image(image_path):
    img = preprocess_image(image_path)
    preds = model.predict(img)
    decoded = decode_predictions(preds, top=3)[0]

    # Return best guess
    label = decoded[0][1].replace("_", " ")
    confidence = float(decoded[0][2])

    return label, confidence
