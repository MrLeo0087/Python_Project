while True:

    print("What you wanna do: \n\n ---- Task ----\n1. Add Task \n2. Remove Task \n3. Modify Task \n4. Complete task \n\n ---- " \
    "View ---- \n5. View all task \n6. View Complete task \n7. View Remain task \n")
    while True:
        try:
            num = int(input("What you wanna do : "))
            break

        except(ValueError):
            print("Invalid error")


    def add():
        

        # with open("Task.txt","a") as f:
        #     f.write("---- All Task list ---- \n")
            

        a = int(input("How many task you want to add : "))
        
        for i in range(a):
            taskadd = str(input(f"Enter your {i+1} task : "))
            with open("Task.txt","a") as f:
                f.write(f"{i+1}. {taskadd} \n")

    def remove():
        print("1. Delete Whole file data \n2. Delete specific task ")

        choice = input("Choose one : ")

        if choice == '1':
            open("Task.txt","w").close()


        elif choice == '2':
            a = input("Which task you want to delete : ")
            with open("Task.txt", "r") as f:
                lines = [line.strip().split(". ", 1)[-1] for line in f if line.strip()]

                task = []

            for i in lines:
                if a!= i:
                    task.append(i)  

            


            with open("Task.txt", "w") as f:
                for i, t in enumerate(task,1):
                    f.write(f"{i}. {t} \n")



        
                


    def view():
        with open("Task.txt","r") as f:
            contain = f.read()

        print(contain)

        
            
            

    match num:
        case 1:
            add()

        case 2:
            remove()

        case 5:
            view()

    choice = input("Wanna continue : y/n : ")

    if choice != 'y':
        break

