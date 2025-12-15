from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from modules.image_processing import preprocess_image
import numpy as np

# -----------------------------
# ImageNet → Shopping mapping
# -----------------------------
LABEL_MAP = {
    "spotlight": "LED spotlight",
    "torch": "LED flashlight",
    "desk_lamp": "desk lamp",
    "cellular_telephone": "smartphone",
    "notebook": "laptop",
    "headphone": "headphones"
}

model = MobileNetV2(weights="imagenet")

def identify_image(image_path):
    img_array = preprocess_image(image_path)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded = decode_predictions(preds, top=5)[0]

    top_prediction = decoded[0]   # first tuple
    raw_label = top_prediction[1]
    confidence = float(top_prediction[2])

    product_name = LABEL_MAP.get(
        raw_label,
        raw_label.replace("_", " ")
    )

    return product_name, confidence
