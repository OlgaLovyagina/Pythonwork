# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def task_2_1():
    """Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д."""

    from random import randint as r
    n = int(input('Введите количество элементов списка: '))
    list1 = [r(1, 10) for _ in range(n)]
    print(list1)
    new_list = []
    for i in range(0, (len(list1) - 1) // 2 + 1):
        new_list.append(list1[i] * list1[len(list1) - 1 - i])
    print(new_list)


# task_2_1()

# второй вариант с семинара


def task_2_2():
    """Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д."""

    def pairs_multi(nums: list[int]) -> list[int]:
        """Возвращает список произведений пар элементов"""

        paris = []
        iterations = (len(nums) + 1) // 2
        print(iterations)
        for i in range(iterations):
            paris.append(nums[i] * nums[-1 - i])
        return paris

    from random import randint as r

    n = int(input('Введите количество элементов списка: '))
    list1 = [r(1, 10) for _ in range(n)]
    print(list1)
    print(pairs_multi(list1))


task_2_2()
