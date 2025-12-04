print("Welcome to To-do-list .... Python project by Darshan ")

while True:
    print("------------------To-do-list------------------")
    print("Option : \n1. Add task \n2. Remove task \n3. Modify task \n4. Complete task \n5. View task")

    while True:
        try:
            num = int(input('Enter your choice : '))
            break
        

        except(ValueError):
            print("Invalid Error")

    def add_task():
        index = 0
        task = []

        try:
            with open("Task.txt","r") as f:
                for line in f:
                    if line.strip():
                        task.append(line.strip())
                        index = index + 1

            # print(f"{task}")

        except(FileNotFoundError):
            index = 0
        while True:  
            try:
                number_of_choice = int(input("Enter how many task you want to add : "))
                break

            except(ValueError):
                print("Invalid Input")

        for i in range(number_of_choice):
            taskadd = str(input(f"Enter {i+1} task : "))

            dublicate_check = [t.split(". ", 1)[1] for t in task]

            if taskadd in dublicate_check:
                print("Task already exist! ")
                continue

            with open("Task.txt",'a') as f:
                f.write(f"{index+1}. {taskadd}\n")

                task.append(f"{index+1}. {taskadd}")
                index+=1
                print("Task added!")

    def remove_task():
        try:
            task = []
            while True:  
                try:
                    choice = int(input("1. Entire file \n2. Specific task \nChoose :  "))
                    break

                except(ValueError):
                    print("Invalid Input")

            
            if choice == 1:
                with open("Task.txt",'w') as f:
                        pass

            elif choice == 2:
                while True:  
                    try:
                        method = int(input("1. Using index \n2. Using task name \nChoose :  "))
                        break

                    except(ValueError):
                        print("Invalid Input")

                if method==1:
                    index_number = int(input("Enter index number: "))
                    with open("Task.txt",'r') as f:
                        for line in f:
                            if line.strip():
                                task.append(line.strip())


                    if 1<=index_number<=len(task):
                        remove_task = task.pop(index_number-1)

                    task_only= [t.split(". ",1)[1] for t in task]
                    with open('Task.txt','w') as f:
                        for i, tasks in enumerate(task_only,1):
                            f.write(f'{i}. {tasks}\n')

                    print(f"task remove!")

                elif method==2:
                    new_task = []
                    task_name = str(input('Enter full task name : '))
                    with open("Task.txt",'r') as f:
                        for line in f:
                            if line.strip():
                                task.append(line.strip())

                    task_only= [t.split(". ",1)[1] for t in task]

                    for task in task_only:
                        if task!=task_name:
                            new_task.append(task)
                    
                    with open('Task.txt','w') as f:
                        for i, tasks in enumerate(new_task,1):
                            f.write(f'{i}. {tasks}\n')

                    print(f"task remove!")
            
        except(FileNotFoundError):
            print("Add some task firstly !")

    def modify_task():
        try:
            task=[]
            count = 0
            choice = int(input("1. Using index \n2. Using task name \nChoose : "))
            if choice == 1:
                task_index = int(input("Enter the task number : "))

                with open("Task.txt",'r') as f:
                    for line in f:
                        if line.strip():
                            task.append(line.strip())
                    
                final_task = [t.split(". ",1)[1] for t in task]
                if 1<=task_index<=len(task):
                    new_task = str(input("Enter your new task : "))
                    for i in final_task:
                        if i == new_task:
                            count +=1

                    if count == 0:
                        final_task[task_index-1] = new_task

                else:
                    print("Enter valid index! ")

                with open("Task.txt",'w') as f:
                    for i,tasks in enumerate(final_task,1):
                        f.write(f"{i}. {tasks}\n") 

            elif choice == 2:
                task = []
                new_task = []

                with open("Task.txt",'r') as f:
                    for line in f:
                        if line.strip():
                            task.append(line.strip())

                task_no_index= [t.split(". ",1)[1] for t in task]

                old_task = str(input("Enter old task : "))
                modify = str(input("Enter new task : "))

                for i in task_no_index:
                    if i == modify:
                        print("task alreasy exit")
                        new_task = task_no_index[:]
                        break

                    if i != old_task:
                        new_task.append(i)

                    elif i == old_task:
                        new_task.append(i.replace(old_task,modify))

                with open("Task.txt", "w") as f:
                    for i, t in enumerate(new_task,1):
                        f.write(f"{i}. {t}\n")
        except(FileNotFoundError):
            print("Add some task first!")
            
            

    def complete_task():
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
        
                        


    def view_task():
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
            add_task()

        case 2: 
            remove_task()

        case 3:
            modify_task()

        case 4:
            complete_task()

        case 5:
            view_task()

    choice = input("Wanna continue (y\\n) : ")

    if choice !='y':
        break

    

