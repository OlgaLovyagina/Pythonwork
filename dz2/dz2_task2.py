# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4,
# тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число N: '))
list_fac = []
fac = 1
for i in range(N):
    i += 1
    fac = i * fac
    list_fac.append(fac)
print(list_fac)

# второй вариант с семинара
#
# import math
#
# n= int(input('Введите число N: '))
# multiplication = [math.factorial(i) for i in range(1, n+1)]
# print (f'List of multiplication^ {multiplication}')



