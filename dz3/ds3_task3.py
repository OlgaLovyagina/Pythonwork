# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# (максимальное значение у числа 1.2, минимальное у 10.01)
def task_3_1():
    """Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов."""

    list1 = [input() for _ in range(int(input('введите вещественные числа')))]
    maximum = 0
    minimum = 1
    for el in list1:
        if '.' in el:
            if float('0.' + el.split('.')[1]) < minimum:
                minimum = float('0.' + el.split('.')[1])
        else:
            if float('0.' + el.split('.')[1]) > maximum:
                maximum = float('0.' + el.split('.')[1])

    print(maximum - minimum)


task_3_1()


