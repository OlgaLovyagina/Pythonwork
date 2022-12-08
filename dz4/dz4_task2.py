#  Задайте натуральное число N. Напишите программу, которая составит список простых
#  множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

def task_1_():
    n = int(input('введите натуральное число: '))
    if n == 1:
        print(1)
    list1 = []
    for i in range(1, n + 1):
        if n % i == 0:
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    break
            else:
                list1.append(i)
    print(list1)


task_1_()

# решение с семинара как пример работы с функциями
# def dividers(a: int, uniq: bool = False) -> list[int]:
#
#
#     """"Возвращает список простых делителей числа.
#     uniq = True вернет список уникальных делителей"""
#     i = 2
#     dividers = []
#     while a != 1:
#         while a % i == 0:
#             dividers.append(i)
#             a //= i
#         i += 1
#     if uniq:
#         return list(set(dividers))
#     else:
#         return dividers
#
# a = 81
# print(f'Список натуральных делителей числа {a}:{dividers(a)}')
# print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')
