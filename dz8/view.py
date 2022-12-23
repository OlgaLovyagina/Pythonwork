# Модуль для ввода/вывода информации


def choose() -> str:
    """"Выбор режима работы приложения"""
    print('1 - решить пример\n\
    2- найти корни уравнения\n\
    3 - упростить многочлен\n\
    4 - показать историю')
    return input('выбран пункт: ')

def get_expr() -> str:
    """"Запрашивает у пользователя задачу"""
    return input('введите задачу: ')


def show_res(res: str):
    """Выводит результат"""
    print(res)


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    print('такого режима нет')


def show_history(history: str):
    """Выводит истроию оперций"""
    print(history.split('\n'))
    for i in history.split('\n'):
        print(i.replace(';', ' -> result: '))
