# 1 - Створіть функцію, яка повертає всі непарні числа в діапазоні.
# Функція приймає початок і кінець діапазону як параметри.
# Використовуйте механізм генераторів усередині функції.

# def returns_odd_numbers(s, e):
#     for n in range(s, e + 1):
#         if n % 2 != 0:
#             yield n
#
# s_range = int(input("Введіть початок діапазону: "))
# e_range = int(input("І його кінець: "))
# odd_nums = returns_odd_numbers(s_range, e_range)
# res = list(odd_nums)
#
# if res:
#     print(f"\nНепарними числами в вашому діапазоні є: {res}")
#
# else:
#     print("Перепрошую, але у вашому діапазоні немає парних чисел!")

# -----------------------------------------------------------------------

# 2 - Створіть функцію, яка повертає всі значення кратні п'яти в діапазоні.
# Функція приймає початок і кінець діапазону як параметри.
# Використовуйте механізм генераторів усередині функції.

# def returns_multiples_of_five(s, e):
#     for n in range(s, e + 1):
#         if n % 5 == 0:
#             yield n
#
# s_range = int(input("Введіть початок діапазону: "))
# e_range = int(input("І його кінець: "))
# multiples_of_five = returns_multiples_of_five(s_range, e_range)
# res = list(multiples_of_five)
#
# if res:
#     print(f"\nЧисла, кратні 5 у діапазоні у вашому діапазоні є: {res}")
#
# else:
#     print("Перепрошую, але у вашому діапазоні немає чисел, які кратні 5!")


def range_palindromes(s, e):
    for p in range(s, e + 1):
        if str(p) == str(p)[::-1]:
            yield p

s_range = int(input("Введіть початок діапазону: "))
e_range = int(input("І його кінець: "))
res = range_palindromes(s_range, e_range)

if res:
    print("Ось ваші паліндроми в вашому діапазоні: ")

    for n in res:
        print(n, end = " ")

else:
    print("Перепрошую, але у вашому діапазоні немає чисел, які кратні 5!")

