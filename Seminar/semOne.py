﻿# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет


print('Напишите программу, которая принимает на вход цифру, обозначающую день недели, \nи проверяет, является ли этот день выходным.')
num = int(input('Введите число от 1 до 7: ' ))
if num <= 5 and num > 0:
	print('Нет')
elif num == 6 or num == 7:
	print('Да')
else:
	print('Неверный диапазон числа')



#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for i in range(2):
	for k in range(2):
		for l in range(2):
			print(not(i or k or l) == (not i and not k and not l))    # Попытался но чтот не получилось
				
				

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
print('Напишите программу, которая принимает на вход координаты точки (X и Y), \nпричём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, \nв которой находится эта точка (или на какой оси она находится).')
x = int(input('Введите число для x:' ))
y = int(input('Введите число для y:' ))
if x != 0 and y != 0 and x > 0 and y > 0:
	print(1)
elif x != 0 and y != 0 and x < 0 and y > 0:
	print(2)
elif x != 0 and y != 0 and x < 0 and y < 0:
	print(3)
elif x != 0 and y != 0 and x > 0 and y < 0:
	print(4)
else:
	print('Введите число больше нуля!')



#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print('Напишите программу, которая по заданному номеру четверти, показывает диапазон \nвозможных координат точек в этой четверти (x и y).')
num_a = int(input('Введите число от 1 до 4: ' ))
if num_a == 1:
	print('x > 0 and y > 0')
elif num_a == 2:
	print('x < 0 and y > 0')
elif num_a == 3:
	print('x < 0 and y < 0')
elif num_a == 4:
	print('x > 0 and y < 0')
else:
	print('Вы ввели некорректное значение')


#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
print('Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
#from math import sqrt

x_a = int(input('Введите первое число для координаты А:' ))
y_a = int(input('Введите второе число для координаты А:' ))
x_b = int(input('Введите первое число для координаты В:' ))
y_b = int(input('Введите второе число для координаты В:' ))

print(round(((x_a - x_b)**2 + (y_a - y_b) **2)**0.5, 2))




