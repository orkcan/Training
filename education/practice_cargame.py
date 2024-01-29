command_check=False

while command_check is False:
    decision = str(input("Please type help to see choices: ").lower())
    print("I don't understand that. Please type help to see: ")
    if decision == "help":
        command_check=True
        break


while command_check is True:
        print("Here are your choices:")
        print("-Start : to start the car")
        print("-Stop : to stop the car")
        print("-Quit : to exit")
        decision = str(input("Please type help to see choices or please pick a function from the list: "))
        if decision == "start":
            print("Car started")
        elif decision == "stop":
            print("Car stopped")
        elif decision== "quit":
            print("Exiting the program")
            break
        else:
            print("I don't understand that command")


