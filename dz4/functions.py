import sympy
from random import randint as rnd

def create_polinom(k: int, simple: bool = True) -> str:
    '''генегирует полином со случайными коэффициентами степени к
    simple = Folse вернет полином без сокращения нулевых коэффициентов'''
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0, 100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)

def create_pol_file(polinom: str, filemane: str = 'new'):
    '''записывает полином в файл, дополнительно можно указать имя файла'''
    with open(f'{filemane}.txt', 'w') as f:
        f.write(polinom)
