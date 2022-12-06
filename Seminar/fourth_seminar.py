#Домашняя работа
def task4_1():
# Вычислить число ПИ c заданной точностью
# d *Пример: * - при d = 0.0001, π = 3.1415.
    import math
    a = math.pi
    d = 0.0001
    print(f'При d = {d}, π = {str(a)[:len(str(d))]}')
#task4_1()

def task4_2():
#Задайте последовательность чисел.Напишите программу, которая выведет список
#неповторяющихся элементов исходной последовательности.
    a_lst = list(map(int, input().split()))
    b_lst = [x for i, x in enumerate(a_lst) if i == a_lst.index(x)]
    print(b_lst)
#task4_2()

def task4_3():
#Задана натуральная степень k.Сформировать случайным образом список коэффициентов(значения
#от 0 до 100) многочлена и записать в файл многочлен степени k(до 6 степени).*
# *Пример: *
# - k = 2 = > 2 * x² + 4 * x + 5 = 0 или x² + 5 = 0 или 10 * x² = 0
    import random
    k = 4
    res = ''
    for i in range(k, 1, -1):
        res = res + f'{random.randint(0, 100)} * {k} ** {i}'
        res = res + random.choice([' + ', ' - '])
    res = res + f'{random.randint(0, 100)} * x + {random.randint(0, 100)} = 0'
    print(res)


    with open('file.txt', 'w') as data:
        data.write(res)
task4_3()



##################Работа на семинаре######################
def taskin41():
#Задайте строку из набора чисел.Напишите программу, которая покажет большее и меньшее
# число.В качестве символа - разделителя используйте пробел
    str1 = '1 5 84 9 6 88'
    str1 = str1.strip()
    for i in range(len(str1)):
        print(min(int(str1)))
#taskin41()


def taskin42():
# Найдите корни квадратного уравнения
# Ax² + Bx + C = 0 двумя способами
    string = '-5x^2 - 7x + 3 = 0'

    a, lit1, b, lit2, c = string[:-3].split()
    b = lit1 + b
    c = lit2 + c
    a = int(a[:a.index('x')])
    b = int(b[:b.index('x')])
    c = int(c)
    D = b * b - 4 * a * c
    if D < 0:
        print('Корней нет')
    elif D == 0:
        print(f'x = {-b / (2 * a)}')
    else:
        print(f"x1 = {round((-b + D ** 0.5) / (2 * a), 2)}, x2 = {round((-b - D ** 0.5) / (2 * a), 2)}")

# taskin41()

def taskin43():
#Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
#     import math
#     print(math.lcm(x, y))
# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
    import  math
    def find_mult(num):
        multipliers = []
        div = 2
        while num > 1:
            while num % div == 0:
                multipliers.append(div)
                num //= div
            div += 1
        return  multipliers

    a, b = 18, 48
    multipliers_a = find_mult(a)
    multipliers_b= find_mult(b)


    print(multipliers_a,multipliers_b)
    res=1
    for i in set(multipliers_b).intersection(set(multipliers_a)):
        res*=i
    print('Наибольший общий делитель:',res)
    print(round(a*b/res))



# taskin43()

