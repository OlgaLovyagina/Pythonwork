# Вычислить число Пи c заданной точностью d
#
# *Пример:*
#
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415
def task_1_():
    from math import pi
    d = input('введите точность d: ')
    a = len(d)
    print(str(pi)[0:a])


task_1_()