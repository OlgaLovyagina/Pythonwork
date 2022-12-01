# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в
# файле file.txt в одной строке одно число.(для продвинутых - с файлом,
# вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

with open("file.txt", "r") as f:
    index_file = f.read().split('\n')
index_file = list(map(int, index_file))

print(index_file)

n = int(input('задайте N: '))
list1 = [i for i in range(-n, n + 1)]
multiply = 1
for p in index_file:
    multiply *= list1[p]
print(list1)
print(f'Произведение элементов по индексу в файле = {multiply}')

