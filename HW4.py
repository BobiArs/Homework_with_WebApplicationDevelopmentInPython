# 1 - Розробіть програму для керування електронною бібліотекою.
# У бібліотеці зберігаються книги, які мають назву, автора, рік видання та кількість сторінок.
#
# Створіть клас Book, який представлятиме окрему книгу,
# та реалізуйте для нього магічні методи, щоб з об’єктами
# класу можна було працювати так само зручно, як із вбудованими типами Python.
#
# Частина 1. Створення класу
# Створіть клас Book з атрибутами:
#
# title — назва книги;
#
# author — автор;
#
# year — рік видання;
#
# pages — кількість сторінок.
#
# Реалізуйте такі магічні методи:
#
# Метод
#
# Завдання
#
# __init__()
#
# Ініціалізувати атрибути книги.
#
# __str__()
#
# Повернути зручний для користувача опис книги.
#
# __repr__()
#
# Повернути формальне представлення об’єкта для налагодження.
#
# __len__()
#
# Повернути кількість сторінок книги.
#
# __eq__()
#
# Перевірити, чи однакові дві книги за назвою та автором.
#
# __lt__()
#
# Порівняти дві книги за кількістю сторінок.
#
# __add__()
#
# Повернути сумарну кількість сторінок двох книг.
#
# __contains__()
#
# Перевірити, чи міститься певне слово в назві книги.
#
# Сортування книг. Реалізуйте порівняння, щоб можна було сортувати список книг за кількістю сторінок.
#
# Перевірка коректності даних. Забороніть створення книг із від’ємною кількістю сторінок або некоректним роком видання.
#
# Підрахунок книг. Додайте до класу магічний метод __bool__(), який визначатиме, чи є книга непорожньою (наприклад, чи має вона додатну кількість сторінок).

class Book:
    def __init__(self, title: str, author: str, year: int, pages: int):
        if year <= 0:
            raise ValueError("Рік видання повинен бути більшим за 0")

        if pages < 0:
            raise ValueError("К-ть сторінок не може бути від'ємною")

        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self) -> str:
        return f"«{self.title}» — {self.author} ({self.year} р., {self.pages} ст.)"

    def __repr__(self) -> str:
        return (f"Данні про книгу:"
                f"\n Назва = '{self.title}'"
                f"\n Автор = '{self.author}'"
                f"\n Рік = {self.year}"
                f"\n Та сторінки = {self.pages})")

    def __len__(self) -> int:
        return self.pages

    def __eq__(self, oth: object) -> bool:
        if not isinstance(oth, Book):
            return NotImplemented

        return self.title == oth.title and self.author == oth.author

    def __lt__(self, oth: "Book") -> bool:
        if not isinstance(oth, Book):
            return NotImplemented

        return self.pages < oth.pages

    def __add__(self, oth: "Book") -> int:
        if not isinstance(oth, Book):
            return NotImplemented

        return self.pages + oth.pages

    def __contains__(self, word: str) -> bool:
        return word in self.title

    def __bool__(self) -> bool:
        return self.pages > 0

print("--- 1. Створення книг та валідація ---")
book1 = Book("Кобзар", "Тарас Шевченко", 1840, 115)
book2 = Book("Тигролови", "Іван Багряний", 1944, 320)
book3 = Book("Гаррі Поттер", "Дж. К. Роулінг", 1997, 320)
book_empty = Book("Порожній чернетка", "Невідомий", 2026, 0)
print(f"Було створено книгу: {book1}")

print("\n--- 2. Перевірка __repr__ ---")
print(repr(book2))

print("\n--- 3. Використання len() та додавання через + ---")
print(f"Сторінок у Кобзарі: {len(book1)}")
print(f"Сума сторінок двох книг (Кобзар + Тигролови): {book1 + book2}")

print("\n--- 4. Порівняння на рівність (назва та автор) ---")
same_book = Book("Кобзар", "Тарас Шевченко", 2010, 500)
print(f"Чи однакові дві книги 'Кобзар'?: {book1 == same_book}")

print("\n--- 5. Перевірка __contains__ (оператор in) ---")
print(f"Чи є слово 'Поттер' у назві book3?: {'Поттер' in book3}")
print(f"Чи є слово 'Володар' у назві book3?: {'Володар' in book3}")

print("\n--- 6. Сортування списку книг ---")
library = [book2, book1, book3, book_empty]
print("До сортування:")
for b in library: print(f" - {b.title}: {b.pages} ст.")

library.sort()

print("\nПісля сортування (за зростанням сторінок):")
for b in library: print(f" - {b.title}: {b.pages} ст.")

print("\n--- 7. Перевірка логічного значення (__bool__) ---")
print(f"Чи є книга '{book1.title}' дійсною?: {bool(book1)}")
print(f"Чи є книга '{book_empty.title}' дійсною?: {bool(book_empty)}")