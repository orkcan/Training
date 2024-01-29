#classes
#types:numbers strings booleans// lists, dictionaries

numbers = [1,2,3,4,5]
#numbers.pop()
#print(numbers)

class Point:
    #define all the func and methods here in a class
    def __init__(self, x, y, z):     ## called a constructor. used to construct or create an obj
        self.x=x
        self.y=y
        self.z=z

    def move(self):
        print("Move")

    def draw(self):
        print("draw")

    def calculate_sum(numbers):
        return sum(numbers)

    def square_sum(numbers):
        return sum(numbers)**2

    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

    def calculate_sum(numbers):
        return sum(numbers)

    def square_sum(numbers):
        return sum(numbers)**2

    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

point1 = Point(10,20,30)
point1.x= 11
point1.y=20
print(point1.x)
print(point1.z) # no attribute "z" Use consctructor(init in def func) for this

point1.draw()
#point2 = Point()
print(point1.y)
