import os

def save_uploaded_image(file):
    path = os.path.join("static", "uploads")
    os.makedirs(path, exist_ok=True)

    file_path = os.path.join(path, file.filename)
    file.save(file_path)
    return file_path
