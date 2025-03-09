# Сутності:

# Field: Базовий клас для полів запису.
# Name: Клас для зберігання імені контакту. Обов'язкове поле.
# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
# AddressBook: Клас для зберігання та управління записами.

# Функціональність:
# AddressBook:Додавання записів.
# Пошук записів за іменем.
# Видалення записів за іменем.
# Record:Додавання телефонів.
# Видалення телефонів.
# Редагування телефонів.
# Пошук телефону.

from decorators import error_decorator

@error_decorator(default_result=None)
class Contact():
    def __init__(self, args):
        self.name = args[0]
        self.phone = args[1]
    def __str__(self):
        return f'Contact name: {self.name}, phone: {self.phone}'


class ContactList():
    def __init__(self):
        self.contacts = []    

    @error_decorator(default_result=None)
    def add_contact(self, contact):
        self.contacts.append(contact)
        return (f'{contact} added.')
    def all_contacts(self):
        for i in self.contacts: 
            print(f'{i}')

    @error_decorator(default_result=None)
    def get_phone(self, args):
        name = args[0]
        result = ''
        for i in self.contacts:
            if i.name == name: 
                result += f'Contact {i.name} phone is {i.phone} \n'
        if result == '': result = 'Phone not found'
        return result
    
    @error_decorator(default_result=None)
    def change_contact(self, args):
        name = args[0]
        phone = args[1]
        result = 'Phone not found'
        for i in self.contacts:
            if i.name == name: 
                i.phone = phone
                result = f'Contact updated to {i}'
        return result

@error_decorator(default_result=[None, None])
def parse_input(user_input):    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = ContactList()
    print("Welcome to the assistant bot!")
    while True:
         user_input = input("Enter a command: ")
         command, *args = parse_input(user_input)
         match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                contact = Contact(args)
                if contact != None:
                    print(contacts.add_contact(contact))                                  
            case "change":
                result = contacts.change_contact(args)                 
                if result != None:
                    print(result)
            case "phone":
                result = contacts.get_phone(args)
                if result != None:
                    print(result)
            case "all":
                contacts.all_contacts()


if __name__ == "__main__":
    main()

