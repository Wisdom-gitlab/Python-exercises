while True:
    print("\nWelcome to your To_do_list App\nSelect Option:\n  \n1.Add task\n2.View tasks\n3.Delete task\n4.Mark a completed task\n5.Exit App\n")
    

    option = int(input("Enter option: "))

    
    if option == 1:
        while True:
         a = open("lists.txt", "a")
         task = input("Enter your task: ")
         a.write(task + "\n")
         a.close()
         print("Task added")

         choice = input("Return to menu? (yes/no): ").lower()
         if choice == "yes":
            break
         else:
            continue


    elif option == 2:
        a = open("lists.txt", "r")
        num = 1

        for line in a.readlines():
            print(f"{num}. {line.strip()}")
            num += 1

        a.close()

        choice = input("Return to menu? (yes/no): ").lower()
        if choice == "yes":
            continue
        else:
            break


    elif option == 3:
        b = int(input("Enter task number to delete: "))

        a = open("lists.txt", "r")
        lines = a.readlines()
        a.close()

        a = open("lists.txt", "w")

        num = 1
        for line in lines:
            if num != b:
                a.write(line)
            num += 1

        a.close()
        print("Task deleted")

        choice = input("Return to menu? (yes/no): ").lower()
        if choice == "yes":
            continue
        else:
            break

    
    elif option == 4:
        b = int(input("Enter task number to mark as complete: "))

        file = open("lists.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("lists.txt", "w")

        num = 1
        for line in lines:
            task = line.strip()

            if num == b:
                file.write(task + " [DONE]\n")
            else:
                file.write(task + "\n")

            num += 1

        file.close()
        print("Task marked as completed!")

        choice = input("Return to menu? (yes/no): ").lower()
        if choice == "yes":
            continue
        else:
            break
    elif option==5:
        exit()


    else:
        print("Invalid input")