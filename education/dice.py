import random


# a=random.randint(1,6)
# b=random.randint(1,6)
# for i in range(6,6):
#     a=random.randint(1,6)
# b=random.randint(1,6)
# dice=(a,b)
# print(dice)
# dice=(a,b)
# print(dice)


# this one below is wrong:
# class Dice:
#     def roll(self):
#         random.randint(a=random.randint(1, 6), b=random.randint(1, 6))
#
Dice2=()

class Dice2:
    def roll(self):
        a=random.randint(1,6)
        b=random.randint(1,6)
        return a,b #ın a functıon you can skip () to return a tuple


# dice1 = Dice()
dice2 = Dice2().roll()
# dice1.roll()

# print(dice1.roll())
print(dice2)
