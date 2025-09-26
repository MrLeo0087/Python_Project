while True:

    print("What you wanna do: \n\n ---- Task ----\n1. Add Task \n2. Remove Task \n3. Modify Task \n4. Complete task \n\n ---- " \
    "View ---- \n5. View Task")
    while True:
        try:
            num = int(input("What you wanna do : "))
            break

        except(ValueError):
            print("Invalid error")


    def add():
        

        # with open("Task.txt","a") as f:
        #     f.write("---- All Task list ---- \n")

        try:
            with open("Task.txt",'r') as f:
                lines = [line.strip().split(". ", 1)[-1] for line in f if line.strip()]
                index = len(lines)
        
        except FileNotFoundError:
            index = 0

        while True:
            try:
                a = int(input("How many task you want to add : "))
                break

            except(ValueError):
                print("invalid")
        
        for i in range(a):
            taskadd = str(input(f"Enter your {i+1} task : "))
            with open("Task.txt","a") as f:
                f.write(f"{index+1}. {taskadd} \n")
                index+=1

    def remove():
        try:
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
        except FileNotFoundError:
            print("\nFirstly Add some task")


    def modify():
        try:
            pre = input("Old Task : ")
            new = input("New Task : ")
            with open("Task.txt",'r') as f:
                lines = [line.strip().split(". ", 1)[-1] for line in f if line.strip()]

            line = []

            for i in lines:
                if pre != i:
                    line.append(i)

                elif pre == i:
                    line.append(i.replace(pre,new))

            with open("Task.txt", "w") as f:
                for i, t in enumerate(line,1):
                    f.write(f"{i}. {t} \n")

        except FileNotFoundError:
            print("\nFirstly Add some task")


    def complete():
        try:
            a = input("Which task completed : ")
            with open("Task.txt","r") as f:
                lines = [line.strip().split(". ", 1)[-1] for line in f if line.strip()]

            for i in lines:
                if a == i:
                    with open("Complete.txt","a") as f:
                        f.write(f"{a}\n")

                    with open("Task.txt", "r") as f:
                        lines = [line.strip().split(". ", 1)[-1] for line in f if line.strip()]

                    task = []

                    for i in lines:
                        if a!= i:
                            task.append(i)  

                


                    with open("Task.txt", "w") as f:
                        for i, t in enumerate(task,1):
                            f.write(f"{i}. {t} \n")

        except FileNotFoundError:
            print("\nFirstly Add some task")
        
                        


    def view():
        try:
            with open("Task.txt","r") as f:
                contain = f.read()
                print("\nRemain Task : ")
                print(f"{contain}\n")
                
        except FileNotFoundError:
            print("No Remain Task")

        try:
            with open("Complete.txt","r") as cf:
                contain_cf = cf.read()
                print("complete Task : ")
                print(f"{contain_cf}\n")

        except FileNotFoundError:
            print("No Complete Task")
   

    match num:
        case 1:
            add()

        case 2:
            remove()

        case 3:
            modify()

        case 4:
            complete()

        case 5:
            view()

    choice = input("Wanna continue : y/n : ")

    if choice != 'y':
        break

