def task3_1():
    # Напишите программу, которая найдёт произведение пар чисел списка.
    # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    #
    # *Пример:*
    #
    #     - [2, 3, 4, 5, 6] => [12, 15, 16];
    #     - [2, 3, 5, 6] => [12, 15]
    from random import randint
    num = []
    num1 = []
    result = 0
    count = 0
    res = -1
    for i in range(9):
        num.append(randint(1, 9))
    print(num)
    odd = len(num) / 2
    if len(num) % 2 == 0:
        for i in range(int(odd)):
            result = num[count] * num[res]
            num1.append(result)
            res -= 1
            count += 1
        print(num1)
    if len(num) % 2 != 0:
        for i in range(int(odd + 1)):
            result = num[count] * num[res]
            num1.append(result)
            res -= 1
            count += 1
        print(num1)
    #task3_1()

def task3_2():
# Задайте список из вещественных чисел.Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#     *Пример: *
#  [1.1, 1.2, 3.1, 5.1, 10.01] = > 0.19

    import random
    num = []
    num_2 = []
    num_max = 0
    num_min = 0
    for i in range(5):
        num.append(random.uniform(1.0, 9.9))
    print(num)
    result = 0
    for i in num:
        result = i - int(i)
        num_2.append(result)
    num_max = max(num_2)
    num_min = min(num_2)
    print(num_max - num_min)
    #task3_2()

def task3_3():
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример: *
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

    b = int(input('Введите число: ' ))
    c = str('')
    while b > 0:
        num_a = int(b % 2)
        c = str(num_a) + c
        b //= 2
    print(c)
    print(bin(b))
    #task3_3()

def task3_4():
    # Задайте число.Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    #
    # *Пример: *
    # - для k = 8 список будет выглядеть
    # так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

    f1 = 1
    f2 = 1
    fn1 = 1
    fn2 = -1
    lst = [f1, f2]
    lst2 = [0, fn1, fn2]
    n = int(input('Введите число: '))

    while n > 2:
        f1, f2 = f2, f1 + f2
        fn1, fn2 = fn2, fn1 - fn2
        lst.append(f2)
        lst2.append(fn2)
        n -= 1
    lst2.reverse()
    print(lst)
    print(lst2)
    lst3 = lst2 + lst
    print(lst3)

task3_4()