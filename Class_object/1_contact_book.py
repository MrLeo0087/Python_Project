
'''
1. Contact Book
Concepts: Classes basics
Build a Contact class with name, phone, and email. Store contacts in a list. Support adding, viewing, and deleting
contacts through a simple menu.
Hints:
- Start with just __init__ and a __str__ method so printing a contact looks clean.
- Use a list of Contact objects, not a list of dicts - that's the whole point of the exercise.
- Write a delete_contact(name) function that loops and removes by match.

DATE : Thursday, July 21, 2026

'''

class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'Name: {self.name}  Phone: {self.phone}  Email: {self.email}'
    

# user_1 = Contact('darshan', 9848334818, 'satorugojo0087@gmail.com')

# print(user_1.name)



class ContactBook:
    def __init__(self, contact_list=None):
        if contact_list is None:
            self.contact_list = []

        else:
            self.contact_list = contact_list
        self.menu()

    def menu(self):
        print('''Choose one action : \n
              1. Add contact\n
              2. Remove contact \n
              3. View contact \n
              4. Search contact \n
              5. Press any key for exit''')
        
        choice = input('Enter your choice : ')

        if choice == '1':
            self.add_contact()

        elif choice == '2':
            self.remove_contact()

        elif choice == '3':
            self.view_contact()

        elif choice == '4':
            self.search_contact()

        else:
            print('Thank you for using contact book !')

    def add_contact(self):
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')

        new_obj = Contact(name,phone,email)



        self.contact_list.append(new_obj)
        print('Contact added \n')
        self.menu()

    def remove_contact(self):
        name = input('Name: ')
        found = False

        for i in self.contact_list:
            if  name == i.name:
                self.contact_list.remove(i)
                print(f'Removed {i} from contact list')
                found = True

        if not found:
            print(f"Contact not avaliable for {name}")

        self.menu()


    def view_contact(self):
        print('\nYour contact are: ')

        for i in self.contact_list:
            print('\n',i)


        self.menu()

    def search_contact(self):
        name = input('Name: ')
        found = False
        for i in self.contact_list:
            if  name == i.name:
                    print(f'Contact Found : \n {i}')
                    found = True

        if not found:
            print(f'Contact not avaliable for {name}')
              

        self.menu()



        

        

book1 = ContactBook()
# add a contact through the menu, then exit
book2 = ContactBook()
# check book2.contact_list before adding anything - is it empty, or does it already have book1's contact?
