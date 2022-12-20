def add_new(contact):
    try:
        with open('book.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{contact}')

    except FileNotFoundError:
        with open('book.txt', 'w', encoding='utf-8') as book:
            book.write(f'\n{contact}')

def get_base():
    with open('book.txt', 'r', encoding='utf-8') as book:
        return book.read()
