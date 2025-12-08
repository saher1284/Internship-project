import os
from PIL import Image
import numpy as np

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img = img.convert("RGB")
    img_array = np.array(img) / 255.0
    return img_array.reshape(1, 224, 224, 3)
