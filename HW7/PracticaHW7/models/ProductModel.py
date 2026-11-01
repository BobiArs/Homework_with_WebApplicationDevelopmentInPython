from PracticaHW7.Product_Component import Product

class ProductModel:
    def __init__(self):
        self.products = [
            Product("Банани", "🍌", 45, 4.8),
            Product("Яблука", "🍎", 35, 4.7),
            Product("Апельсини", "🍊", 55, 4.9),
            Product("Полуниця", "🍓", 120, 4.8),
            Product("Чорниця", "🫐", 150, 4.9),
            Product("Виноград", "🍇", 95, 4.6),
            Product("Ківі", "🥝", 80, 4.7),
            Product("Манго", "🥭", 140, 4.8),
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, prod_id):
        for product in self.products:
            if product.id == str(prod_id):
                return product

        return None

    def create_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            return product

        return None