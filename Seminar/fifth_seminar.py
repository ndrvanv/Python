# Домашняя работа
def task5_1():
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


# task5_1()
def task5_2():
    # Создайте программу для игры с конфетами человек против человека. Условие
    # задачи: На столе лежит 2021 конфета.Играют два игрока делая ход друг после
    # друга.Первый ход определяется жеребьёвкой.За один ход можно забрать не более
    # чем 28 конфет.Все конфеты оппонента достаются сделавшему последний ход.Сколько
    # конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    # a) Добавьте игру против бота
    # b) Подумайте как наделить бота ""интеллектом""

    from random import randint

    def imput_nam(name):
        x = int(input(f'{name} Введите колличество конфет от 1 до 28: '))
        while 1 > x or x > 28:
            x = int(input(f'{name} Введите количество не превышающее значение 28 и не ниже 1: '))
        return x

    def output(name, k, total, counter):
        print(f'Ход у {name} взял конфет {k} осталось {total} и с общим количеством {counter} у игрока')

    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')
    total = int(input('Введите количество конфет: '))

    flag = randint(0, 1)
    if flag:
        print(f'Первый ход у {player1}')
    else:
        print(f'Первый ход у {player2}')

    counter1 = 0
    counter2 = 0

    while total > 28:
        if flag:
            k = imput_nam(player1)
            total -= k
            counter1 += k
            flag = False
            output(player1, k, total, counter1)
        else:
            k = imput_nam(player2)
            total -= k
            counter2 += k
            flag = True
            output(player1, k, total, counter2)

    if flag:
        print(f'Выиграл игрок {player1}')
    else:
        print(f'Выиграл игрок {player2}')


# task5_2()

def task5_3():
    # Создайте программу для игры в ""Крестики-нолики"".
    board = list(range(1, 10))
    wins_coordinate = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

    def draw_board():
        print('-------------')
        for i in range(3):
            print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')

    def take_input(player_signal):
        while True:
            value = input('Выберите позицию: ' + player_signal + ' ? ')
            if not (value in '123456789'):
                print('Такого числа нет в таблице. Повторите пожалуйта!')
                continue  # Возвращает на начало цикла while
            value = int(value)
            if str(board[value - 1]) in 'XO':
                print('Эта клетка уже занята')
                continue
            board[value - 1] = player_signal
            break

    def check_win():
        for each in wins_coordinate:
            if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
                return board[each[1] - 1]
        else:
            return False

    def main():
        counter = 0
        while True:
            draw_board()
            if counter % 2 == 0:
                take_input('X')
            else:
                take_input('O')
            if counter > 3:
                winner = check_win()
                if winner:
                    draw_board()
                    print(winner, 'выиграл!')
                    break
            counter += 1
            if counter > 8:
                draw_board()
                print('Ничья!')
                break

    main()


# task5_3()

def task5_4():
    # Реализуйте RLE алгоритм: реализуйте модуль сжатия
    # и восстановления данных.

    # first step we create function for enconding data
    def rle_encode(data):
        encoding = ''
        prev_char = ''
        count = 1
        if not data: return ''
        for char in data:
            # if not match the previous and current characters
            if char != prev_char:
                # then add the count and characters to our enconding
                if prev_char:
                    encoding += str(count) + prev_char
                count = 1
                prev_char = char
            else:
                # increment our counter if characters do match
                count += 1
        else:
            # finish our enconding
            encoding += str(count) + prev_char
            return encoding
    input_data = rle_encode('JJJJJJUUUUUUUSSSSSTTTTTDOOOOOIIIIIIIIT')
    print(input_data)

    # function for decoding
    def rle_decoding(data):
        decode = ''
        count = ''
        for char in data:
            # if character is numerical
            if char.isdigit():
                # append it to our count
                count += char
            else:
                # otherwise if character non-numerical
                # we have to expand it for encondig
                decode += char * int(count)
                count = ''
        return decode
    inp_data = rle_decoding('6J7U5S5T1D5O8I1T')
    print(inp_data)



task5_4()


# Работа на семинаре
def taskin5_1():
    # В файле находится N натуральных чисел, записанных через
    # пробел.Среди чисел не хватает одного, чтобы выполнялось
    # условие
    # A[i] - 1 = A[i - 1].Найдите это число.
    import random

    lst = [i for i in range(10)]
    lst.pop(random.randint(0, 9))

    search_num = [i for i in range(1, len(lst)) if lst[i] - lst[i - 1] > 1][0]

    with open('filein5_1.txt', 'w') as file:
        file.write(' '.join(list(map(str, lst))))

    with open('filein5_1.txt', 'r') as file:
        lst_new = file.read().split()
        print(*lst_new)

    lst_new.insert(search_num, search_num)
    print(*lst_new)

    with open('filein5_1.txt', 'a') as file:
        file.write('\n' + ' '.join(list(map(str, lst_new))))


# taskin5_1()

def taskin5_2():
    # Дан список чисел.Создайте список, в который попадают числа, описываемые
    # возрастающую последовательность.Порядок элементов менять
    # нельзя. [1, 5, 2, 3, 4, 6, 1, 7] = > [1, 2, 3]
    # или[1, 5] или[1, 4, 6, 7] и т.д.

    lst = [1, 5, 2, 3, 4, 6, 1, 7]

    res_lst = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > max(res_lst):
            res_lst.append(lst[i])

    print(res_lst)

# taskin5_2()
