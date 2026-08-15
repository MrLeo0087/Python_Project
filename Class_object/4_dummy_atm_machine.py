class ATM:
    def __init__(self,amount:int=0):
        self.amount = amount
        self.pin = ''
        print('\nwelcome to dummy atm \n')
    def menu(self):
        print('''Choose one operation from index number : 
        1. Update Balance
        2. Set pin
        3. Change pin
        4. Withdraw money
        5. Check balance
        6. Anything for exit''')

        choice = input('\nYour choice : ')

        if choice == '1':
            self.update_balance()

        elif choice == '2':
            self.set_pin()

        elif choice == '3':
            self.change_pin()

        elif choice == '4':
            self.withdraw_money()

        elif choice == '5':
            self.check_balance()

        else:
            print('Thank you for using Dummy atm.')

    def update_balance(self):
        if self.pin.strip():
            pin = input('Enter pin: ')
            if pin == self.pin:
                new_balance = int(input('Enter your new amount : '))
                self.amount = new_balance
                print(f'Successfully set new balance to {self.amount}')

            else:
                print('Pin incorrect')

        else:
            print('Set pin first')

        self.menu()
                

    def set_pin(self):
        if not self.pin.strip():
            pin = input('Enter your pin : ')
            self.pin = pin
            print('Pin set successfully')

        else:
            print('Pin already set. cannot reset now.')

        self.menu()


    def change_pin(self):
        if self.pin.strip():
            old_pin = input('Enter your old pin : ')
            if old_pin == self.pin:
                new_pin = input('Enter your new pin : ')
                self.pin = new_pin

            else:
                print('Pin does not match. Try again!')
        else:
            print('First set pin')
        self.menu()
    def withdraw_money(self):
        if self.amount > 0:
            pin = input('Enter your pin : ')
            if pin == self.pin:
                ask_money = int(input('Enter your money : '))
                if ask_money<self.amount:
                    self.amount -=ask_money
                    print(f'{ask_money} withdraw successfully.')

            
                else:
                    print(f'Not enough money. You have only {self.amount} rupees')
            else:
                print('Wrong pin')
        else:
            print('You have zero balance')

        self.menu()
        

    def check_balance(self):
        print(f'You have {self.amount} rupess')
        self.menu()
          



atm = ATM()
atm.menu()