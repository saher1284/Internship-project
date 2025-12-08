from flask import Flask, render_template, request
from modules.image_recognition import identify_image
from modules.price_search import compare_prices
from modules.utils import save_uploaded_image

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    if "image" not in request.files:
        return "No file uploaded."

    file = request.files["image"]
    img_path = save_uploaded_image(file)

    product_name, confidence = identify_image(img_path)
    price_results = compare_prices(product_name)

    return render_template(
        "results.html",
        product=product_name,
        confidence=round(confidence * 100, 2),
        results=price_results,
        img_path=img_path
    )

if __name__ == "__main__":
    app.run(debug=True)
