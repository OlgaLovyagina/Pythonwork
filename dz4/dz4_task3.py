# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

list1 = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
for i in list1:
    if list1.count(i) == 1:
        print(i, end=' ')

# вариант с семинара, более продвинуто)))

# from random import randint
#
# list2 = [randint(1, 7) for i in range(12)]
# print(list2)
# list2 = [i for i in list2 if list2.count(i) == 1]
# print(list2)
