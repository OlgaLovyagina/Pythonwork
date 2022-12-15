# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4,
# тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число N: '))
# list_fac = []
# fac = 1
# for i in range(n):
#
#     fac = (i + 1) * fac
#     list_fac.append(fac)
# print(list_fac)

import math
n = int(input('Введите число N: '))
fac = [(i + 1) * math.factorial(i) for i in range(n)]
fac = [(i + 1) * math.factorial(i) for i in range(n)]
print(fac)
