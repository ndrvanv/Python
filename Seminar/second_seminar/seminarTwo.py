#1. �������� ���������, ������� ��������� �� ���� ������������ ����� � ���������� ����� ��� ����.
#    *������:*
#     6782 -> 23
#     0.56 -> 11

count = 0
a = int(input('������� �����: ' ))
while a > 0:
    b = a % 10     
    count += b
    a = a // 10   # ������� ��������� �����
print(count)

#������ ������
num = abs(float(input('������� �����: ' )))
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
    a = int(input('������� �����: ' ))
    while a > 0:
        b = a % 10
        total += b
        a = a // 10   # ������� ��������� �����
        print(total)

#2. �������� ���������, ������� ��������� �� ���� ����� N � ������ ����� ������������ ����� �� 1 �� N.
#*������:*
#����� N = 4, ����� [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#import math
#a = int(input('������� �����: ' ))
#count = 1
#while a >= count:
#    print(math.factorial(count), end=' ')
#    count = count + 1

#3. ������� ������� �� n ����� ������������������ (1 + (1/n))^n � �������� �� ����� �� �����.
#*������:*
#��� n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#���������� ������� ��� �������� ������� � �������  ����� �� �����.

#n = int(input('������� �����: ' ))
#d = {}
#for i in range(1, n+1):
#    d[i]= (1 + (1/i))**i
#print(d)
#print(sum(d.values()))


#4. ������� ������ �� N ���������, ����������� ������� �� ���������� [-N, N]. 
#������� ������������ ��������� �� ��������� ��������. ������� �������� � ����� file.txt � ����� ������ ���� �����.

with open('for_two_seminar.txt', 'r') as data:
    f = data.read().split('\n')
n = int(input('������� �����: ' ))
result = 1
spisok = []
for i in range(-n, n + 1):
    spisok.append(i)
print(f"������ �� �����: {f}")
print(f"������ �� -N �� N: {spisok}")
for k in f:
    result *= spisok[int(k)]
print(f'������������ ����� {result}')

##5. ���������� �������� ��������� ���������� �����.(�� ��������� ���������� ��������� � ��������)
#import datetime

#def genRandInt(First, Second):
#    if not isitence(First, int) or not isitence(Second, int):
#        raise ValueError("First and Second value must be int type")
#    date_now = str(datatime.datetime.now())[-6] #����� ����������� �� ����
#    integer_for_gen = int(data_now + data_now) # ������������ � ���� int
#    generated = 0 # ���������� ��� ����������������� �����
#    while(True):
#        if generated >= First and generated <= Second:
#            break
#        elif First == Second:
#            return First
#        integer_for_gen /= 19 #����� ������������ �� 19
#        generated = integer_for_gen #������������
#    return int(round(generated)) 

#print(genRandInt(2, 100))
