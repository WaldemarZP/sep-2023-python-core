#strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
#
# res = []
#
# for i in st:
#     if i.isdigit():
#         res.append(i)
#
# print(res)

# print(','.join(i for i in st if i.isdigit()))

#################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34' #введена строка
# 23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'

# res = []
# x = ''
#
# for i in st:
#     if i.isdigit():
#         x += i
#     elif x.isdigit():
#         res.append(x)
#         x = ''
# else:
#     if x.isdigit():
#         res.append(x)
#
# print(res)

# print(', '.join(''.join(i if i.isdigit() else ' ' for i in st).split()))

#################################################################################

# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'

# res = []
#
# for letter in greeting:
#     res.append(letter.upper())
#
# print(res)

# print([i.upper() for i in greeting])

#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# res = []
#
# for i in range(50):
#     if i % 2 == 1:
#         res.append(i ** 2)
#
# print(res)

# print([i ** 2 for i in range(50) if i % 2 == 1])

#################################################################################

# function
#
# - створити функцію яка виводить ліст

# def create_list(l):
#     for i in l:
#         print(i)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_of_three(a, b, c):
#     max_num = max(a, b, c)
#     print(max_num)
#     return max_num

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def min_max(*args):
#     min_num = min(args)
#     max_num = max(args)
#     print(max_num)
#     return min_num

# - створити функцію яка повертає найбільше число з ліста

# def main():
#     return (max(list(i for i in range(10))))
#
# x = main()
# print(x)

# def max_of_list(l):
#     return max(l)
#
# x = max_of_list([1,2,3,4])
# print(x)


# - створити функцію яка повертає найменьше число з ліста

# def main():
#     return (min(list(i for i in range(10))))
#
# x = main()
# print(x)

# def min_of_list(l):
#     return min(l)
#
# x = min_of_list([1,2,3,4,5,6,7,8,9])
# print(x)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# list1 = [1,2,3,4,5,6,7,8,9,10]
# def func():
#     return sum(list1)
#
# x = func()
# print(x)

# def sum_of_list(l):
#     return sum(l)
#
# x = sum_of_list([1,2,3,4,5,6,7,8,9])
# print(x)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# list1 = [1,2,3,4,5,6,7,8,9,10]
# def func():
#     return sum(list1) / len(list1)
#
# x = func()
# print(x)

# def avg_of_list(l):
#     return sum(l)/len(l)
#
# x = avg_of_list([1,2,3,4,5,6,7,8,9])
# print(x)


################################################################################################
# 1)Дан list:
# list1 = [22, 3,5,2,8,2,-23, 8,23,5]

# - знайти мін число

# def find_min_from_list():
#     print(min(list1))

# - видалити усі дублікати

# def remove_duplicates():
#     print(list(set(list1)))

# - замінити кожне 4-те значення на 'X'

# def to_x():
#     res = []
#     for i, v in enumerate(list1):
#         if not (i + 1) % 4:
#             v = 'X'
#             res.append(v)
#         else:
#             res.append(v)
#     print(res)
#
# to_x()

# print(['X' if (i + 1) % 4 == 0 else v for i, v in enumerate(list1)])
# print(['X' if not (i + 1) % 4 else item for i, item in enumerate(list1)])

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

# def square(n):
#     for i in range(n):
#         if i == 0 or i == n - 1:
#             print('*' * n)
#         else:
#             print('*' + ' ' * (n - 2) + '*')

# 3) вывести табличку множення за допомогою цикла while

# x = int(input("Enter a number: "))
#
# for i in range(1, 11):
#     print(f'{x} x {i} = {x * i}')

# def multi_table():
#     size = 9
#     i = 1
#     while i <= size:
#         j = 1
#         while j <= size:
#             res = i * j
#             # print('  ' if res//10 else '   ', end='')
#             # print(res, end='')
#             print(f'{res:4}', end='')
#             j += 1
#         i += 1
#         print()

# 4) переробити це завдання під меню

# while True:
#     print('1) Find min from list')
#     print('2) Remove duplicates')
#     print('3) All 4th number to X')
#     print('4) Square table')
#     print('5) Multi table')
#     print('6) Exit')
#
#     choice = input('Enter your choice: ')
#
#     if choice == '1':
#         find_min_from_list()
#     elif choice == '2':
#         remove_duplicates()
#     elif choice == '3':
#         to_x()
#     elif choice == '4':
#         square(4)
#     elif choice == '5':
#         multi_table()
#     elif choice == '6':
#         break