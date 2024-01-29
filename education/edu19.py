def user_greeting(first_name, age):             #first name and age are parameters
    first_name = input("What is your name?:")
    age = input("What is your age?")
    print(f'naber {first_name} kardeş!yaşın da {age} olmuş')

print("hosgeldin")
user_greeting("Joseph",age=31)       #joseph and 31 are arguments
#keyword arguments should be after the positional arguments. python does it this way
calc_cost=(total=50,shiping=5,discount=0.1)  #using keyword arguments to inc. readability

print("gule gule")

#def calc_cost(total, shipping, discount):
#    cost = total + shipping - (total * discount)
#    return cost
