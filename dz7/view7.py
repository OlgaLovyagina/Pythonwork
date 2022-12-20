def choose_mode():
    return input('введите режим работ (1 - добавление, 2 - поиск)')

def new_cotact():
    name = input('введите имя: ')
    phone_num = input('введите номер: ')
    return f'{name} || {phone_num}'

def show_found(result):
    print('результаты поиска: ')
    for i in result:
        print(i)
def cotact_to_s():
    cotact_to_s = input(' введите имя или телефон для поиска : ')
    return cotact_to_s