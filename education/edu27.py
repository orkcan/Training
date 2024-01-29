import random

for i in range(3):   # running for 3 times
    random.random()
    # /print(random.random())
    print(random.randint(0,10))
# print(random.randrange(1,100,1))


members=['Joseph','Joseph2','Joseph3']
leader = random.choice(members)
print(leader)