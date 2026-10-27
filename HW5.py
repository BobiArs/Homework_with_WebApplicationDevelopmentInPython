# 1 - Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину),
# клас Blender (містить інформацію про блендер),
# клас MeatGrinder (містить інформацію про м'ясорубку).
# Кожен із класів має містити необхідні для роботи методи

# class Device:
#     def __init__(self, brand: str, power: int):
#         self.brand = brand
#         self.power = power
#         self.is_on = False
#
#     def t_on(self):
#         if not self.is_on:
#             self.is_on = True
#             print(f"Пристрій {self.brand} було увімкнено в розетку")
#
#         else:
#             print(f"Пристрій {self.brand} вже працює")
#
#     def t_off(self):
#         if self.is_on:
#             self.is_on = False
#             print(f"Пристрій {self.brand} вимкнено")
#
#         else:
#             print(f"Пристрій {self.brand} вже був вимкнений")
#
#     def __str__(self):
#         if self.is_on:
#             stat = "Увімкнено"
#
#         else:
#             stat = "Вимкнено"
#
#         return f"Маємо пристрій {self.brand}, у якого потужність: {self.power}W, та статус: {stat})"
#
# class CoffeeMachine(Device):
#     def __init__(self, brand: str, power: int, water_cap: float):
#         super().__init__(brand, power)
#         self.water_cap = water_cap
#         self.coffee_beans_lvl = 100
#
#     def b_coffee(self, coffee_type: str):
#         if not self.is_on:
#             print(f"У {self.brand} помилка: спочатку треба увімкнути кавомашину!")
#             return
#
#         if self.coffee_beans_lvl < 20:
#             print(f"У {self.brand} помилка: закінчилися зерна! Треба досипати кави")
#             return
#
#         print(f"{self.brand} меле зерна та гріємо воду...")
#         print(f"{self.brand} - ваше ароматне {coffee_type} ГОТОВЕ")
#         self.coffee_beans_lvl -= 20
#
# class Blender(Device):
#     def __init__(self, brand: str, power: int, speeds_count: int):
#         super().__init__(brand, power)
#         self.speeds_count = speeds_count
#         self.curr_speed = 0
#
#     def set_speed(self, speed: int):
#         if not self.is_on:
#             print(f"У {self.brand} помилка: Ви походу забули увімкнути блендер")
#             return
#
#         if 1 <= speed <= self.speeds_count:
#             self.curr_speed = speed
#             print(f"Для {self.brand} встановлено швидкість {self.curr_speed} із {self.speeds_count}")
#
#         else:
#             print(f"У {self.brand} помилка: такої швидкості немає для цього блендера")
#
#     def blend(self):
#         if self.curr_speed == 0:
#             print(f"У {self.brand} помилка: виберіть швидкість перед збиванням суміші")
#
#         else:
#             print(f"{self.brand} Вжжжж (Імітація)! Блендер почав збивати смузі на швидкості такій то - {self.curr_speed}!")
#
# class MeatGrinder(Device):
#     def __init__(self, brand: str, power: int, has_rev: bool):
#         super().__init__(brand, power)
#         self.has_rev = has_rev
#
#     def grind_meat(self, meat_type: str):
#         if not self.is_on:
#             print(f"У {self.brand} помилка: м'ясорубка зараз вимкнена!")
#             return
#
#         print(f"{self.brand} переробляє {meat_type} на фарш...")
#
#     def activate_reverse(self):
#         if not self.is_on:
#             print(f"У {self.brand} помилка: пристрій зараз вимкнено!")
#             return
#
#         if self.has_rev:
#             print(f"У {self.brand} було увімкнено реверс! Очищаємо снек назад...")
#
#         else:
#             print(f"У цій моделі {self.brand} немає функції реверсу, тому без нього")
#
# print("1) === ТЕСТ КАВОМАШИНИ ===")
# delonghi = CoffeeMachine("DeLonghi", 1450, 1.8)
# print(delonghi)
# delonghi.b_coffee("Еспресо")
# delonghi.t_on()
# delonghi.b_coffee("Капучино")
# delonghi.t_off()
#
# print("\n2) === ТЕСТ БЛЕНДЕРА ===")
# philips = Blender("Philips", 800, 5)
# philips.t_on()
# philips.blend()
# philips.set_speed(3)
# philips.blend()
# philips.t_off()
#
# print("\nі 3) === ТЕСТ М'ЯСОРУБКИ ===")
# moulinex = MeatGrinder("Moulinex", 2000, has_rev=True)
# moulinex.t_on()
# moulinex.grind_meat("куряче філе")
# moulinex.activate_reverse()
# moulinex.t_off()

# 2 - Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас Frigate (містить інформацію про фрегат),
# клас Destroyer (містить інформацію про есмінця),
# клас Cruiser (містить інформацію про крейсер).
# Кожен із класів має містити необхідні для роботи методи

# class Ship:
#     def __init__(self, name: str, max_speed: int):
#         self.name = name
#         self.max_speed = max_speed
#         self.anchor_down = True
#
#     def raise_anchor(self):
#         if self.anchor_down:
#             self.anchor_down = False
#             print(f"Корабель {self.name} підняв якір і готовий до виходу в море")
#
#         else:
#             print(f"Корабель {self.name} вже на ходу, якір піднято")
#
#     def drop_anchor(self):
#         if not self.anchor_down:
#             self.anchor_down = True
#             print(f"Корабель {self.name} скинув якір та зупинився")
#
#         else:
#             print(f"Корабель {self.name} вже стоїть на якорі")
#
#     def __str__(self):
#         status = "Стоїть на якорі" if self.anchor_down else "На ходу в морі"
#         return f"По ітогу маємо корабель {self.name}, у якого макс. швидкість: {self.max_speed} вузлів, та статус: {status}"
#
# class Frigate(Ship):
#     def __init__(self, name: str, max_speed: int, sonar_range: int):
#         super().__init__(name, max_speed)
#         self.sonar_range = sonar_range
#         self.torpedoes_count = 6
#
#     def scan_for_submarines(self):
#         if self.anchor_down:
#             print(f"У {self.name} помилка: спочатку треба знятися з якоря, щоб патрулювати!")
#             return
#
#         print(f"{self.name} увімкнув сонар і сканує воду на {self.sonar_range} км у пошуках підводних човнів...")
#
#     def launch_torpedo(self):
#         if self.torpedoes_count <= 0:
#             print(f"У {self.name} помилка: закінчилися торпеди! Треба повернутися на базу")
#             return
#
#         self.torpedoes_count -= 1
#         print(f"{self.name} — Плі! (Імітовано) Торпеду випущено. Залишилось торпед ось стільки: {self.torpedoes_count} шт")
#
# class Destroyer(Ship):
#     def __init__(self, name: str, max_speed: int, missiles_count: int):
#         super().__init__(name, max_speed)
#         self.missiles_count = missiles_count
#         self.curr_missiles = missiles_count
#
#     def load_missiles(self):
#         self.curr_missiles = self.missiles_count
#         print(f"Для {self.name} повністю поповнено боєкомплект. Заряджено ракет: {self.curr_missiles}")
#
#     def fire_missile(self, target: str):
#         if self.anchor_down:
#             print(f"У {self.name} помилка: Ви походу забули знятися з якоря перед атакою, не забувайте")
#             return
#
#         if self.curr_missiles > 0:
#             self.curr_missiles -= 1
#             print(f"{self.name} випустив крилату ракету по цілі '{target}'. І був влучний удар!")
#
#         else:
#             print(f"У {self.name} помилка: немає ракет для залпу! Викличте метод load_missiles для фіксу")
#
# class Cruiser(Ship):
#     def __init__(self, name: str, max_speed: int, has_air_defense: bool):
#         super().__init__(name, max_speed)
#         self.has_air_defense = has_air_defense
#
#     def launch_recon_helicopter(self):
#         if self.anchor_down:
#             print(f"У {self.name} помилка: корабель зараз стоїть на якорі, злітна плумба заблокована!")
#             return
#
#         print(f"З палуби {self.name} піднявся розвідувальний вертоліт для розвідки горизонту")
#
#     def activate_air_defense(self):
#         if self.has_air_defense:
#             print(f"У {self.name} було активовано купол ППО! Небо під повним контролем")
#
#         else:
#             print(f"У цій моделі {self.name} немає посиленої системи ППО, тому захищаємось звичайними зенітками")
#
# print("1) === ТЕСТ ФРЕГАТА ===")
# hetman = Frigate("Гетьман Сагайдачний", 32, 40)
# print(hetman)
# hetman.scan_for_submarines()
# hetman.raise_anchor()
# hetman.scan_for_submarines()
# hetman.launch_torpedo()
# hetman.drop_anchor()
#
# print("\n2) === ТЕСТ ЕСМІНЦЯ ===")
# bucha = Destroyer("Буча", 35, 4)
# bucha.raise_anchor()
# bucha.fire_missile("Ворожий катер")
# bucha.fire_missile("Склад БК")
# bucha.drop_anchor()
#
# print("\nі 3) === ТЕСТ КРЕЙСЕРА ===")
# ukraine = Cruiser("Україна", 30, has_air_defense=True)
# ukraine.raise_anchor()
# ukraine.launch_recon_helicopter()
# ukraine.activate_air_defense()
# ukraine.drop_anchor()

# 3 - Запрограмуйте клас Money (об'єкт класу оперує однією валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.

class Money:
    def __init__(self, whole: int = 0, cents: int = 0, currency: str = "грн"):
        self.whole = whole
        self.cents = cents
        self.currency = currency
        self.normalize()

    def normalize(self):
        if self.cents >= 100:
            self.whole += self.cents // 100
            self.cents = self.cents % 100

        elif self.cents < 0:
            total_cents = self.whole * 100 + self.cents

            if total_cents < 0:
                self.whole = 0
                self.cents = 0

            else:
                self.whole = total_cents // 100
                self.cents = total_cents % 100

    def set_values(self, whole: int, cents: int):
        if whole >= 0 and cents >= 0:
            self.whole = whole
            self.cents = cents
            self.normalize()
            print(f"Значення суми успішно було оновлено! Новий баланс тепер буде становити: {self.whole}.{self.cents:02d} {self.currency}")

        else:
            print("Упс! Помилка: сума грошей в цьому випадку не може бути від' взагалі!")

    def display_money(self):
        print(f"Поточна сума становить: {self.whole}.{self.cents:02d} {self.currency}")

    def __str__(self):
        return f"{self.whole}.{self.cents:02d} {self.currency}"

class Product(Money):
    def __init__(self, name: str, whole: int, cents: int, currency: str = "грн"):
        super().__init__(whole, cents, currency)
        self.name = name

    def reduce_price(self, minus_whole: int, minus_cents: int = 0):
        print(f"\n--- Робимо знижку на товар цей, '{self.name}' ---")
        print(f"Стара ціна: {self.whole}.{self.cents:02d} {self.currency}")
        print(f"Зменшуємо на: {minus_whole}.{minus_cents:02d} {self.currency}")

        current_total_cents = self.whole * 100 + self.cents
        reduce_total_cents = minus_whole * 100 + minus_cents

        if reduce_total_cents < 0:
            print("Помилка: сума знижки не може бути від'ємною!")
            return

        if current_total_cents < reduce_total_cents:
            print(f"Увага: знижка більша за вартість! Товар '{self.name}' тепер стає безкоштовним")
            self.whole = 0
            self.cents = 0

        else:
            self.cents = current_total_cents - reduce_total_cents
            self.whole = 0
            self.normalize()
            print(
                f"Ціну успішно знижено! Нова ціна товару тепер '{self.name}': {self.whole}.{self.cents:02d} {self.currency}")

    def display_product(self):
        print(f"Товар: {self.name} | Ціна по ітогу: {self.whole}.{self.cents:02d} {self.currency}")

print("1) === ТЕСТ КЛАСУ MONEY ===")
wallet = Money(10, 50, "$")
wallet.display_money()
wallet.set_values(15, 175)

print("\n2) === ТЕСТ КЛАСУ PRODUCT ===")
laptop = Product("Ігровий Ноутбук (Asus якийсь)", 25000, 90, "грн")
laptop.display_product()

laptop.reduce_price(1200, 50)

laptop.reduce_price(30000, 0)
laptop.display_product()