#Работа на дом

def task6_1():
    # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

    text = 'абвгдейка идет искать абверу в большой комнате'
    # split a string and put the result
    wordss = text.split(' ')
    piece = 'абв'
    new_text = []
    for word in wordss:
        if piece not in word:
            new_text.append(word)
    print(' '.join(new_text))
    # Сокращенный способ решения задачи
    new_text2 = [word2 for word2 in wordss if piece not in word2]
    print(f'как вариант {" ".join(new_text2)}')
#task6_1()

def task6_2():
#Задайте последовательность чисел.Напишите программу, которая выведет список
#неповторяющихся элементов исходной последовательности.
    a_lst = list(map(int, input().split()))
    b_lst = [x for i, x in enumerate(a_lst) if i == a_lst.index(x)]
    print(b_lst)
#task6_2()

def task6_3():
    # Дан список чисел.Создайте список, в который попадают числа, описываемые
    # возрастающую последовательность.Порядок элементов менять
    # нельзя. [1, 5, 2, 3, 4, 6, 1, 7] = > [1, 2, 3]
    # или[1, 5] или[1, 4, 6, 7] и т.д.

    lst = [1, 5, 2, 3, 4, 6, 1, 7]

    res_lst = [lst[0]]
    # for i in range(1, len(lst)):
    #     if lst[i] > max(res_lst):
    #         res_lst.append(lst[i])
    lst1 = [x for x in range(1, len(lst)) if lst[x] > max(res_lst)]
    print(lst1)
    # print(res_lst)
# task6_3()


def tesk6_1():
    # Напишите программу вычислени арифметического выражения
    # заданного строкой.Используйте операции +, -, /, *.приоритет
    # операций стандартный. *Пример: *
    # 2 + 2 = > 4;
    # 1 + 2 * 3 = > 7;
    # 1 - 2 * 3 = > -5;

    ln_in = input('Введите выражение: ').split()

    print(ln_in)

    def aka_eval(args):
        while len(args) != 1:

            while '*' in args or '/' in args:
                try:
                    prod_index = args.index('*')
                except:
                    prod_index = 100
                try:
                    div_index = args.index('/')
                except:
                    div_index = 100

                if prod_index < div_index:
                    args[prod_index - 1] = int(args[prod_index - 1]) * int(args[prod_index + 1])
                    args.pop(prod_index + 1)
                    args.pop(prod_index)
                else:
                    args[div_index - 1] = int(args[div_index - 1]) / int(args[div_index + 1])
                    args.pop(div_index + 1)
                    args.pop(div_index)

            while '+' in args or '-' in args:
                try:
                    sum_index = args.index('+')
                except:
                    sum_index = 100
                try:
                    deg_index = args.index('-')
                except:
                    deg_index = 100

                if sum_index < deg_index:
                    args[sum_index - 1] = int(args[sum_index - 1]) + int(args[sum_index + 1])
                    args.pop(sum_index + 1)
                    args.pop(sum_index)
                else:
                    args[deg_index - 1] = int(args[deg_index - 1]) - int(args[deg_index + 1])
                    args.pop(deg_index + 1)
                    args.pop(deg_index)

        print(args[0])

    aka_eval(ln_in)
tesk6_1()