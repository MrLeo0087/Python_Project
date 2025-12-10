import streamlit as st
import string
import random

st.header(" 🔑 Password Generator and Checker! ")
st.subheader("- By Darshan")

number = ['1','2','3','4','5','6','7','8','9','0']
low_letter = list(string.ascii_lowercase)
upper_letter = list(string.ascii_uppercase)
symbol = ['@','#','$','%','&','*','|','\\','/','?','!']
list_1 = [number,low_letter,upper_letter,symbol]

choice = st.selectbox('Option',['None','Password Generator','Password Strength Checker'])

if choice == 'Password Generator':
    choose = st.selectbox('Choose',['None','Random Password Generator','Password Generator with Hint'])

    if choose == 'Random Password Generator':
        length = st.number_input("Enter Length of Password :", min_value= 4,max_value=20,value=8)

        password = []
        for i in range(length):
            list_2 = random.choice(list_1)
            item = random.choice(list_2)
            password.append(item)
            passwords = "".join(password)

        st.success(passwords)

    if choose == 'Password Generator with Hint':
        length = st.number_input("Enter Length of Password :", min_value= 4,max_value=20,value=8)
        name = st.text_input("Enter Hint : ")
    
        password = []
        list_name = list(name)

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

                st.success(final_password)

        else:
                st.success("Password lenght have to >=hint ")

if choice == 'Password Strength Checker':
    choice = st.text_input("Enter Password : ")

    low_letter_count = 0
    number_count = 0
    upper_letter_count = 0
    symbol_count = 0
    random_count = 0


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
            st.success("STRONG PASSWORD !")

    elif count == 3:
            st.success("MEDIUM PASSWORD! ")

    elif count == 2:
            st.success("WEAK PASSWORD !")

    elif count == 1:
            st.success("VERY WEEK PASSWORD !")

      

       



                

