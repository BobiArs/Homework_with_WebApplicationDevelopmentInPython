# 1 - Для виконання цього завдання обов'язково використовуйте механізм функцій
# вищого порядку (higher order functions).
# Створіть функцію, що відображає лінію (горизонтальну або вертикальну)
# з використанням символу, зазначеного користувачем. Користувач визначає
# символ і яку лінію відображати.
# Сигнатура функції:
# def show_line(symbol, function_to_call)
#
# symbol — символ для відображення.
# function_to_call — функція для відтворення лінії (вертикальна лінія або
# горизонтальна лінія, на один тип лінії — одна функція).

# def horizontal(symbl: str, length: int):
#     print(symbl * length)
#
# def vertical(symbl: str, length: int):
#     for _ in range(length):
#         print(symbl)
#
# def show_line(symbol, function_to_call):
#     length = int(input("Введіть довжину, якою буде лінія: "))
#     if length <= 0:
#         print("Упс! Довжина даної лінії повинна бути більше за 0")
#
#
#     function_to_call(symbol, length)
#
# res = input("Введіть символ, із якого буде лінія: ")
# print("\nЯку лінію будемо відображати?")
# print("1 — Горизонтальну")
# print("2 — Вертикальну")
#
# choice = input("\nІ вашим вибором буде 1 чи 2: ")
#
# if choice == "1":
#     show_line(res, horizontal)
#
# elif choice == "2":
#     show_line(res, vertical)
#
# else:
#     print("Ви обрали неправильний тип лінії!")

# 2 - Напишіть декоратор measure_time, який вимірює час виконання функції та виводить його на екран.
#
# Декоратор потрібно застосувати до функції calculate_sum(), яка обчислює суму всіх чисел від 1 до n.
#
# Вимоги до виконання
# Створіть декоратор measure_time, який приймає функцію як аргумент.
#
# Усередині декоратора створіть вкладену функцію, яка:
#
# фіксує час перед виконанням основної функції;
#
# викликає основну функцію та зберігає її результат;
#
# фіксує час після виконання основної функції;
#
# виводить час виконання у секундах;
#
# повертає результат основної функції.
#
# Використайте модуль time для вимірювання часу.
#
# Застосуйте декоратор до функції calculate_sum(n).
#
# Викличте функцію з аргументом 1_000_000 та виведіть отриману суму.
#
# Приклад очікуваного результату
# text
# Час виконання функції: 0.052 секунди
# Сума чисел: 500000500000

import time

def measure_time(function):
    def wrapper(*args, **kwargs):
        s_time = time.time()
        res = function(*args, **kwargs)
        e_time = time.time()
        exec_time = e_time - s_time

        print(f"Час, який зайняла функція = {exec_time:.3f} сек.")

        return res

    return wrapper

@measure_time
def calc_sum(n):
    tot = 0

    for i in range(1, n + 1):
        tot += i

    return tot

try:
    u_input = input("Введіть якесь число: ")
    res_u = int(u_input.replace('_', ''))
    total_sum = calc_sum(res_u)
    print(f"І сумою чисел буде: {total_sum}")

except ValueError:
    print("Перепрошую, але число треба вводити саме ціле число КОРЕКТНО")
