# Перемешивание списка
# import time
#
#
# def random_without_lib(x):
#     time.sleep(0.001)
#     return int(round(time.time() * 1000) % x)
#
#
# lst = [random_without_lib(10) for i in range(10)]
#
# print(lst)
#
# for i in range(len(lst)):
#     lst[i], lst[random_without_lib(len(lst))] = lst[random_without_lib(len(lst))], lst[i]
#
# print(lst)


# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
word = "qwe"
if lst.count(word) < 2:
    print(-1)
else:
    lst[lst.index(word)] = word[1:]
print(lst.index(word))


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
num = []
result = 0
for i in range(8):
    num.append(randint(0, 9))
print(num)
for i in range(len(num)):
    if i % 2 == 1:
        result += num[i]
print(result)