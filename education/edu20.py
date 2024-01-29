###return statements and functions
def square(number):
    return number*number    #if print would have been used here output=None.

result=square(int(input("Enter a number: ")))
print(result)
print(square(12))



def square(number):
    return number*number


#by default all functions return none
#calculation should be done with return