a = int(input('Введите первое число' ))
b = int(input('Введите второе число' ))
c = int(input('Введите третье число' ))
d = int(input('Введите 4 число' ))
e = int(input('Введите 5 число' ))
print(max(a, b, c, d, e))

#Нахождение наибольшего числа
nums = [int(i) for i in input().split()]
max = nums[0]
for i in range (1, len(nums)):
    if nums[i] > max:
        max = nums[i]
print(max)

lst = []
num = int(input('Введите число' ))
for i in range(-num, num +1):
    lst.append(str(i))
print(', '.join(lst))

x = float(input('Введите дробное число ' ))  #from float to int
y = x % 10
print(int(y))

num_a = input('Введите число str ' )   #from floar to int int throw str
for i in range (len(num_a)):
    if num_a [i] =='.':
        print(num_a[i+1])
        break

x_o = float(input('Введите число' ))
print(int(x_o * 10 % 10))

y_o = int(input())
print((y_o % 5 == 0 and y_o % 10 == 0 or y_o % 15 == 0) and y_o % 30 != 0)

