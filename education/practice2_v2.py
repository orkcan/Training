list1 = []
user_input = input("Please state what would you like to do by typing 'A' for adding, 'R' for removing, 'P' for printing the list or 'Q' for quitting the program: ")
while True:
    if user_input == 'A':
        while True:
            A = input("Enter the number you want to add to the list:")
            if A.isdigit():
                list1.append(int(A))
                print("Thank you for entering a number, the program continues...")
                break
            else:
                print(f"'{A}' cannot be converted to integer.")
                # A = input("Enter the number you want to add to the list:")

    elif user_input == 'R':
        if not list1:
            print('The list is empty, nothing to remove.')
        else:
            while True:
                R = input("Enter the number you want to remove from list:")
                if R.isdigit() and int(R) in list1:
                    list1.remove(int(R))
                    print(str(R) + " has been removed from the list.")
                    print(list1)
                    break
                else:
                    print("This number is either not a number or is not in the list. Please pick a number from the list.")

    elif user_input == 'P':
        print(list1)

    elif user_input == 'Q':
        print("Finished")
        break

    else:
        print("Invalid command. Please enter 'A', 'R', 'P', or 'Q'.")

    user_input = input("Please state what would you like to do by typing 'A' for adding, 'R' for removing, 'P' for printing the list or 'Q' for quitting the program: ")