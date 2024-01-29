list1 = []
user_input = input( "Please state what would you like to do by typing 'A' for adding, 'R' for removing, 'P' for printing the list or 'Q' for quitting the program: ")
while True:
    if user_input=='A':
        A = input("Enter the number you want to add to the list:")
        if A.isdigit():
            list1.append(int(A))
            print("Thank you for entering a number, the program continues...")
            break
        else:
            print(f"'{A}' cannot be converted to integer.")
            A = input("Enter the number you want to add to the list:")
                 # L = str(input("Do you want to quit or continue? Please press 'Q' to finish the program or press 'C' continue: "))
           #elif L == str'C':
          # user_input==user_input
    if user_input == "R":
        R = int(input("Enter the number you want to remove from list:"))
        while R.isdigit()==False or int(R) not in list1:
            R = input("This number is either not a number or is not in the list. Please pick a number from the list.")
            list1.remove(int(R))
            print(str(R) + " has been removed from the list.")
            print(list1)
       # if int(R) in list1:ist1.remove(int(R))
    #             print(str(R) + " has been removed from the list.")
    #
    #         # print("Do you want to quit_")
    #         elif int(R) not in list1:
    #             print("Sorry " + str(R) + " is not in the list. Please pick a number from the list. ")
    #             print(list1)
    #             ## L = input("Do you want to quit or continue? Please press 'Q' to finish the program or press 'C' continue: ")
    elif user_input=='P':
           print(list1)

    elif user_input=='Q':
        print("Finished")
        break
    else:
        print("Invalid command. Please enter 'A', 'R', 'P', or 'Q'.")
    user_input = input( "Please state what would you like to do by typing 'A' for adding, 'R' for removing, 'P' for printing the list or 'Q' for quitting the program: ")
    #else:
    # print("Invalid command. Please enter 'A', 'R', 'P', or 'Q'.")

