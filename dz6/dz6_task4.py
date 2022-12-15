# 1'. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11
#
# number = list(input('введите число: '))
# summ = 0
#
# for current in number:
#     if current == ',' or current == '.' or current == '-':
#         continue
#     else:
#         summ = summ + int(current)
# print(f' сумма цифр числа = {summ}')

number = (input('введите число: ')).replace('.', '')
summa = sum(int(i) for i in number)
print(summa)



