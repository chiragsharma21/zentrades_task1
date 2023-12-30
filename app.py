from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        products = data.get("products", {})
        sorted_products = sorted(products.values(), key=lambda x: int(x["popularity"]), reverse=True)
        return render_template('index.html', products=sorted_products)
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
