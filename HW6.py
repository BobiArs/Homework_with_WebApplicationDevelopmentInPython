# Створіть систему для роботи з товарами інтернет-магазину
# Реалізуйте:
# •	LoggingMixin — метод log(message).
# •	JsonMixin — метод to_json(), який повертає товар у форматі JSON.
# •	DiscountMixin — метод apply_discount(percent), який обчислює ціну зі знижкою.
# •	Product — зберігає назву та ціну товару.
# •	ProductManager — успадковує Product, LoggingMixin, JsonMixin і DiscountMixin.
# Перевірте: товар із ціною 1000 грн після знижки 15% повинен коштувати 850 грн.
# Додатково виведіть ProductManager.__mro__ і поясніть отриманий порядок.

import json

class LoggingMixin:
    @staticmethod
    def log(msg: str):
        print(f"[LOG]: {msg}")

class JsonMixin:
    def to_json(self) -> str:
        return json.dumps(self.__dict__, default = str, ensure_ascii=False)

class DiscountMixin:
    def __init__(self, price: float, name: str):
        self.price = price
        self.name = name

    def apply_discount(self, percent: float):
        if not (0 <= percent <= 100):
            print(f"[ERROR]: % знижки повинен був введений у діапазоні від 0 до 100")
            return

        old_price = self.price
        self.price = old_price * (1 - percent / 100)

        if hasattr(self, "log"):
            self.log(f"На даний товар {self.name}, була застосована знижка у {percent}%.\n"
                     f"Його стара ціна = {old_price} грн, а нова вже = {self.price} грн")

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Товар: {self.name} | І ціна: {self.price} грн"

class ProductManager(Product, LoggingMixin, JsonMixin, DiscountMixin):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

        if hasattr(self, "log"):
            self.log(f"Було створено новий товар в бд менеджера:\n"
                     f"     Продукт {self.name} за {self.price} грн")

print("=== Testing Systems Goods ===")

phone = ProductManager("Смартфон", 1000.0)

print("\n1) Перевірка перевода у JSON:")
print(phone.to_json())

print("\n2) Застосування знижки на 15%:")
phone.apply_discount(15)

print(f"Finally res -> {phone}")

print("\n3) Дослідження порядку вирішення методів (тобто MRO):")
mro_list = ProductManager.__mro__
for index, current_class in enumerate(mro_list, 1):
    print(f" {index}. {current_class}")