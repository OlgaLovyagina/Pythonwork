# Реализуйте алгоритм перемешивания списка
import random
from random import randint
list1 = list(map(int, input('введите элементы списка через пробел: ').split()))
print(f' Первоначальный список {list1}')

for i in range(len(list1)-1):
    n = randint(0, len(list1)-1)
    list1[i], list1[n] = list1[n], list1[i]
print(f' Перемешанный список {list1}')

# второй вариант

import random
list2 = [random.randint(0, 10) for i in range(random.randint(5, 20))]
print(f' Первоначальный список {list2}')
random.shuffle(list2)
print(f' Перемешанный список {list2}')
