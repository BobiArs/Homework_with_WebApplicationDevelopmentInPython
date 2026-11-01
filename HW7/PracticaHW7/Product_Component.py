import uuid

class Product:
    def __init__(self, title, image, price, rating, id = None):
        self.id = str(id) if id else str(uuid.uuid4())
        self.title = title
        self.image = image
        self.price = price
        self.rating = rating

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "image": self.image,
            "price": self.price,
            "rating": self.rating
        }