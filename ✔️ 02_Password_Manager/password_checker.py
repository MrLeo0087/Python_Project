while True:
    import string
    import random
    number = ['1','2','3','4','5','6','7','8','9','0']
    low_letter = list(string.ascii_lowercase)
    upper_letter = list(string.ascii_uppercase)
    symbol = ['@','#','$','%','&','*','|','\\','/','?','!']
    list_1 = [number,low_letter,upper_letter,symbol]
    print("Welcome to Password_Manager - Darshan")
    print("1. Generate passoword \n2. Password checker")


    while True:
        try:
            choice = int(input("Enter your choice : "))
            break

        except(ValueError):
            print("Enter valid number")

    if choice == 1:
        choose = int(input("1. Random Password Generate \n2. Password Generate from hint \nChoose : "))

        if choose == 1:

            length = int(input("Length of password : "))

            if 4<=length<=15:
                password = []
                for i in range(length):
                    list_2 = random.choice(list_1)
                    item = random.choice(list_2)
                    password.append(item)
                    passwords = "".join(password)

                print(passwords)
                
            else:
                print("Password length should between 4-15")

        elif choose == 2:
            length = int(input("Length of password : "))

            name = str(input("Give any hint : "))

            list_name = list(name)


            password = []

            for i in list_name:
                name = random.choice([i.upper(),i.lower()])
                password.append(name)

            passwords = "".join(password)

            if length == len(password):
                print(passwords)

            elif length>len(password):
                remain_letter = length-len(password)
                front_letter = remain_letter % 4
                back_letter = remain_letter - front_letter

                front_letter_list = []
                for i in range(front_letter):
                    list_2 = random.choice(list_1)
                    item = random.choice(list_2)
                    front_letter_list.append(item)
                
                back_letter_list = []
                for i in range(back_letter):
                    list_2 = random.choice(list_1)
                    item = random.choice(list_2)
                    back_letter_list.append(item)

                front = "".join(front_letter_list)
                back = "".join(back_letter_list)

                final_password = front+passwords+back

                print(final_password)

            else:
                print("Password lenght have to >=hint ")

        else:
            print("Invalid Input")

    elif choice == 2:

        low_letter_count = 0
        number_count = 0
        upper_letter_count = 0
        symbol_count = 0
        random_count = 0

        # print("Password length have to atleast 5 and maximum 20")
        choice = str(input("Enter Your password : "))

        score = []

        for char in choice:
            if char in low_letter:
                low_letter_count += 1
                

            elif char in number : 
                number_count += 1
                

            elif char in upper_letter:
                upper_letter_count +=1
                

            elif char in symbol:
                symbol_count+=1
                

            else:
                random_count+=1

        score.append(low_letter_count)
        score.append(number_count)
        score.append(upper_letter_count)
        score.append(symbol_count)

        count = 0
                
        for i in score:
            if i != 0:
                count+=1

        if count == 4:
            print("STRONG PASSWORD !")

        elif count == 3:
            print("MEDIUM PASSWORD! ")

        elif count == 2:
            print("WEAK PASSWORD !")

        elif count == 1:
            print("VERY WEEK PASSWORD !")

    a = str(input("Wanna continue (y/n) : "))

    if a!='y':
        print("Thank you ! ")
        break
        



    

                




        
