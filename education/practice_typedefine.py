class Person():                  #first letter in class name always uppercase.(pascal)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi, my name is {self.name} and I am {self.age}. ")

name_input = input("What is your name? ")
age_input = int(input("What is your age? "))
person1=Person(name=name_input, age=age_input)
#person1.name = "Joseph"
#person1.age = 31
print(person1.name)
person1.talk()


person2=Person("bob",39)
person2.talk()