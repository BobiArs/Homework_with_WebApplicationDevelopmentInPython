# FLASK - мінімалістичний фреймворк
from urllib import request

from flask import Flask, render_template, redirect, url_for

from PracticaHW7.Product_Component import Product
from PracticaHW7.models.ProductModel import ProductModel

app = Flask(__name__)
product_model = ProductModel()

@app.route("/")
@app.route("/index")
def home():
    title = "FruitMarket — Натуральні фрукти з усього світу"

    categories = [
        {
            "name": "Всі фрукти", "icon": "🧺", "count": 24, "active": True
        },
        {
            "name": "Ягоди", "icon": "🍓", "count": 6, "active": False
        },
        {
            "name": "Цитрусові", "icon": "🍊", "count": 5, "active": False
        },
        {
            "name": "Кісточкові", "icon": "🍒", "count": 4, "active": False
        },
        {
            "name": "Тропічні", "icon": "🍌", "count": 5, "active": False
        },
        {
            "name": "Яблука та груші", "icon": "🍎", "count": 4, "active": False
        },
    ]

    # Список товарів
    products = product_model.get_all_products()

    return render_template("index.html", title=title, categories=categories, products=products)


@app.route("/product/<prod_id>")
def product_detail(prod_id):
    product = product_model.get_product_by_id(prod_id)
    if not product:
        return "Продукт не знайдено", 404

    return render_template("modal_detail_product.html", product=product)

# GET — форма, POST — збереження
@app.route("/product/create", methods=["GET", "POST"])
def create_product():
    if request.method == "POST":
        title = request.form.get("title")
        image = request.form.get("image", "🍏")
        price = float(request.form.get("price", 0))
        rating = float(request.form.get("rating", 5.0))

        new_product = Product(title=title, image=image, price=price, rating=rating)
        product_model.create_product(new_product)

        return redirect(url_for("home"))

    return '''
        <form method="POST" style="max-width:300px; margin: 40px auto; font-family: sans-serif;">
            <h2>Додати новий фрукт</h2>
            <input type="text" name="title" placeholder="Назва товару" required style="width:100%; margin-bottom:10px; padding:8px;"><br>
            <input type="text" name="image" placeholder="Емодзі (напр. 🍍)" required style="width:100%; margin-bottom:10px; padding:8px;"><br>
            <input type="number" step="0.1" name="price" placeholder="Ціна" required style="width:100%; margin-bottom:10px; padding:8px;"><br>
            <input type="number" step="0.1" name="rating" placeholder="Рейтинг (напр. 4.9)" style="width:100%; margin-bottom:10px; padding:8px;"><br>
            <button type="submit" style="background:#0e8345; color:#fff; border:none; padding:10px 15px; border-radius:6px; cursor:pointer;">Зберегти продукт</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)