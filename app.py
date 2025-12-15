from flask import Flask, render_template, request
import os

from modules.image_recognition import identify_image
from modules.price_search import compare_prices

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', error="No file uploaded")

        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', error="No file selected")

        # Save uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Identify product using your image_recognition module
        product_name, confidence = identify_image(filepath)

        # Fetch price comparison results using your price_search module
        results = compare_prices(product_name)

        # Render results page
        return render_template('results.html',
                               product_name=product_name,
                               confidence=confidence,
                               results=results,
                               uploaded_image=filepath)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
