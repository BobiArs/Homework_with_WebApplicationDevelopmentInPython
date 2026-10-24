# 1 - Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій

# class Car:
#     def __init__(self, model: str = "", year: int = 0, manufacturer: str = "",
#                  engine_volume: float = 0.0, color: str = "", price: float = 0.0):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_volume = engine_volume
#         self.color = color
#         self.price = price
#
#     def input_data(self):
#         print("\n--- Введення даних про автомобіль ---")
#         self.model = input("Введіть назву моделі: ")
#         self.year = int(input("Рік випуску: "))
#         self.manufacturer = input("Виробник: ")
#         self.engine_volume = float(input("Об'єм двигуна (л): "))
#         self.color = input("Колір машинки: ")
#         self.price = float(input("Та ціна ($): "))
#
#     def display_data(self):
#         print("\n--- Характеристики автомобіля по вашим результатам ---")
#         print(f"Модель: {self.model}")
#         print(f"Виробник: {self.manufacturer}")
#         print(f"Рік випуску: {self.year}")
#         print(f"Об'єм двигуна: {self.engine_volume} л")
#         print(f"Колір: {self.color}")
#         print(f"Ціна: ${self.price:,.2f}")
#
#     # Додаткові корисні методи
#     def update_price(self, new_price: float):
#         if new_price >= 0:
#             self.price = new_price
#             print(f"Ціну успішно оновлено. Нова ціна становить: ${self.price:,.2f}")
#
#         else:
#             print("Помилка: ціна авто не може бути від'ємною!")
#
#     def change_color(self, new_color: str):
#         self.color = new_color
#         print(f"Машину було перефарбовано. Тепер її колір: {self.color}")
#
#
# my_car = Car()
#
# while True:
#     print("\n=== ГОЛОВНЕ МЕНЮ ===")
#     print("1. Заповнити/перезаписати дані про авто")
#     print("2. Показати поточні характеристики автомобіля")
#     print("3. Змінити колір автомобіля")
#     print("4. Оновити ціну автомобіля")
#     print("5. Вийти з програми")
#
#     choice = input("\nОберіть дію (1-5): ")
#
#     if choice == "1":
#         my_car.input_data()
#         print("\n Дані успішно збережено!")
#
#     elif choice == "2":
#         my_car.display_data()
#
#     elif choice == "3":
#         if not my_car.model:
#             print(" Треба спочатку заповнити дані про авто (Пункт 1)!")
#             continue
#
#         new_color = input("Введіть новий колір для авто: ")
#         my_car.change_color(new_color)
#
#     elif choice == "4":
#         if not my_car.model:
#             print(" Треба спочатку заповнити дані про авто (Пункт 1)!")
#             continue
#
#         try:
#             new_price = float(input("Введіть нову ціну ($): "))
#             my_car.update_price(new_price)
#
#         except ValueError:
#             print("Помилка: потрібно ввести числове значення!")
#
#     elif choice == "5":
#         print("Дякуємо за використання програми. Бувайте!")
#         break
#
#     else:
#         print("Некоректний вибір! Будь ласка, введіть число від 1 до 5")

# -------------------------------------------------------------------------------------------------------

# 2 - Реалізуйте клас «Книга».
# Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій

# class Book:
#     def __init__(self, title: str = "", author: str = "", year: int = 0,
#                  genre: str = "", pages: int = 0, price: float = 0.0, is_read: bool = False):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.genre = genre
#         self.pages = pages
#         self.price = price
#         self.is_read = is_read
#
#     def input_data(self):
#         print("\n--- Введення даних про книгу ---")
#         self.title = input("Введіть назву книги: ")
#         self.author = input("Автор книги: ")
#         self.year = int(input("Рік видання: "))
#         self.genre = input("Жанр: ")
#         self.pages = int(input("Кількість сторінок: "))
#         self.price = float(input("Ціна ($): "))
#
#         read_input = input("Ви вже прочитали цю книгу? (так/ні): ")
#         self.is_read = read_input in ["так", "yes", "y", "+"]
#
#     def display_data(self):
#         print("\n--- Характеристики книги за вашими результатами ---")
#         print(f"Назва: {self.title}")
#         print(f"Автор: {self.author}")
#         print(f"Рік видання: {self.year}")
#         print(f"Жанр: {self.genre}")
#         print(f"Кількість сторінок: {self.pages}")
#         print(f"Ціна: ${self.price:,.2f}")
#         status = "Прочитано ✅" if self.is_read else "Ще не було прочитано дану 📖"
#         print(f"Статус: {status}")
#
#     def update_price(self, new_price: float):
#         if new_price >= 0:
#             self.price = new_price
#             print(f"Ціну успішно оновлено. Нова вартість книги: ${self.price:,.2f}")
#
#         else:
#             print("Помилка: ціна книги не може бути від'ємною!")
#
#     def toggle_read_status(self):
#         self.is_read = not self.is_read
#         status = "Прочитано ✅" if self.is_read else "Ще не було прочитано дану 📖"
#         print(f"Статус книги було змінено на: {status}")
#
# my_book = Book()
#
# while True:
#     print("\n=== ГОЛОВНЕ МЕНЮ ===")
#     print("1. Заповнити/перезаписати дані про книгу")
#     print("2. Показати інформацію про книгу")
#     print("3. Змінити статус прочитання (прочитано/ні)")
#     print("4. Оновити ціну книги")
#     print("5. Вийти з програми")
#
#     choice = input("\nОберіть дію (1-5): ")
#
#     if choice == "1":
#         my_book.input_data()
#         print("\n Дані про книгу успішно збережено!")
#
#     elif choice == "2":
#         if not my_book.title:
#             print(" Книга ще не створена. Спочатку заповніть дані про неї (Це пункт 1)!")
#             continue
#
#         my_book.display_data()
#
#     elif choice == "3":
#         if not my_book.title:
#             print(" Спочатку вам треба заповнити дані про книгу (Це пункт 1)!")
#             continue
#
#         my_book.toggle_read_status()
#
#     elif choice == "4":
#         if not my_book.title:
#             print(" Спочатку вам треба заповнити дані про книгу (Це пункт 1)!")
#             continue
#
#         try:
#             new_price = float(input("Введіть нову ціну для книги ($): "))
#             my_book.update_price(new_price)
#
#         except ValueError:
#             print("Помилка: потрібно ввести числове значення!")
#
#     elif choice == "5":
#         print("Дякуємо за використання бібліотекаря. Гарного читання!")
#         break
#
#     else:
#         print("Некоректний вибір! Будь ласка, введіть число від 1 до 5")

# -------------------------------------------------------------------------------------------------------

# 3 - Реалізуйте клас «Стадіон».
# Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Stadium:
    def __init__(self, name: str = "", opening_date: str = "", country: str = "",
                 city: str = "", capacity: int = 0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        print("\n--- Введення даних про стадіон ---")
        self.name = input("Введіть назву стадіону: ")
        self.opening_date = input("Дата відкриття (наприклад, 12.05.2018): ")
        self.country = input("Країна: ")
        self.city = input("Місто: ")
        self.capacity = int(input("Та місткість (кількість глядачів): "))

    def display_data(self):
        print("\n--- Характеристики стадіону за вашими результатами ---")
        print(f"Назва стадіону: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Розташування: {self.city}, {self.country}")
        print(f"Місткість: {self.capacity:,} глядачів")

    def update_capacity(self, new_capacity: int):
        if new_capacity >= 0:
            self.capacity = new_capacity
            print(f"Місткість успішно оновлено! Нова місткість: {self.capacity:,} глядачів")

        else:
            print("Помилка: місткість не може бути від'ємною!")

    def rename_stadium(self, new_name: str):
        old_name = self.name
        self.name = new_name
        print(f"Стадіон успішно перейменовано з '{old_name}' на '{self.name}'")


my_stadium = Stadium()

while True:
    print("\n=== ГОЛОВНЕ МЕНЮ ===")
    print("1. Заповнити/перезаписати дані про стадіон")
    print("2. Показати інформацію про стадіон")
    print("3. Перейменувати стадіон (зміна назви/спонсора)")
    print("4. Оновити місткість (після реконструкції)")
    print("5. Вийти з програми")

    choice = input("\nОберіть дію (1-5): ")

    if choice == "1":
        my_stadium.input_data()
        print("\n Дані про стадіон успішно збережено!")

    elif choice == "2":
        if not my_stadium.name:
            print(" Стадіон ще не створено. Спочатку заповніть дані (Пункт 1)!")
            continue

        my_stadium.display_data()

    elif choice == "3":
        if not my_stadium.name:
            print(" Спочатку заповніть дані про стадіон (Пункт 1)!")
            continue

        new_name = input("Введіть нову назву для стадіону: ")
        my_stadium.rename_stadium(new_name)

    elif choice == "4":
        if not my_stadium.name:
            print(" Спочатку заповніть дані про стадіон (Пункт 1)!")
            continue

        try:
            new_cap = int(input("Введіть нову місткість глядачів: "))
            my_stadium.update_capacity(new_cap)

        except ValueError:
            print("Помилка: потрібно ввести ціле число!")

    elif choice == "5":
        print("Дякуємо за використання програми. До зустрічі на трибунах!")
        break

    else:
        print("Некоректний вибір! Будь ласка, введіть число від 1 до 5.")