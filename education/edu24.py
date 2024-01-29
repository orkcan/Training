# class Dog:
#    def walk(self):
#        print("walk doggie")
#
#
# class Cat
#    def walk(self):
#        print("walk kittie")
#
"  #duplicated walk method here. here's how to fix it: inheritance"


# Define a base class called Mammal
class Mammal:
    # Method in the Mammal class to simulate walking
    def walk(self):
        print("walk")


# Define a subclass called Dog, inheriting from the Mammal class
class Dog(Mammal):
    # Method specific to Dog class for barking
    def bark(self):
        print("woof woof")


# Define another subclass called Cat, also inheriting from the Mammal class
class Cat(Mammal):
    # Method specific to Cat class for being annoying (making a cat sound)
    def be_annoying(self):
        print("meeeeeooooowwww meeeeeooowwww")
    #pass   # when python expects addition to cat class use this to bypass


dog1 = Dog()
dog1.walk()
cat1=Cat()
cat1.be_annoying()

# pip install openpyxl xls app for python