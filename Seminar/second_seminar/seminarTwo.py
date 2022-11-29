#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#    *Пример:*
#     6782 -> 23
#     0.56 -> 11

count = 0
a = int(input('Введите число: ' ))
while a > 0:
    b = a % 10     
    count += b
    a = a // 10   # убираем последнюю цифру
print(count)

#Второй способ
num = abs(float(input('Введите число: ' )))
if isinstance(num, float):
    while round(num) != num:
        num *= 10
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
            print(int(total))
elif isinstance(num, int):
    total = 0
    a = int(input('Введите число: ' ))
    while a > 0:
        b = a % 10
        total += b
        a = a // 10   # убираем последнюю цифру
        print(total)

#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#*Пример:*
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#import math
#a = int(input('Введите число: ' ))
#count = 1
#while a >= count:
#    print(math.factorial(count), end=' ')
#    count = count + 1

#3. Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#*Пример:*
#Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#Необходимо сложить все значения словаря и вывести  сумму на экран.

#n = int(input('Введите число: ' ))
#d = {}
#for i in range(1, n+1):
#    d[i]= (1 + (1/i))**i
#print(d)
#print(sum(d.values()))


#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

with open('for_two_seminar.txt', 'r') as data:
    f = data.read().split('\n')
n = int(input('Введите число: ' ))
result = 1
spisok = []
for i in range(-n, n + 1):
    spisok.append(i)
print(f"Список из файла: {f}")
print(f"Список от -N до N: {spisok}")
for k in f:
    result *= spisok[int(k)]
print(f'Произведение равно {result}')

##5. Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки связанные с рандомом)
#import datetime

#def genRandInt(First, Second):
#    if not isitence(First, int) or not isitence(Second, int):
#        raise ValueError("First and Second value must be int type")
#    date_now = str(datatime.datetime.now())[-6] #Выбор милисекунды из даты
#    integer_for_gen = int(data_now + data_now) # миллисекунды к типу int
#    generated = 0 # переменная для сгеннерированного числа
#    while(True):
#        if generated >= First and generated <= Second:
#            break
#        elif First == Second:
#            return First
#        integer_for_gen /= 19 #Делим миллисекунды на 19
#        generated = integer_for_gen #Присваивание
#    return int(round(generated)) 

#print(genRandInt(2, 100))
