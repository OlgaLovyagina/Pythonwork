import logger7
import model7
import view7

def run():
    while True:
        mode = view7.choose_mode()
        if mode == '1':
            contact = view7.new_cotact()
            logger7.add_new(contact)
        elif mode == '2':
            contact = view7.cotact_to_s()
            base = logger7.get_base()
            result = model7.search_contact(base, contact)
            view7.show_found(result)
