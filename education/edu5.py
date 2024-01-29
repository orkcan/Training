price=35

print(price>10 and price<100)
print(price>10 or price<35)
print(price>100 or price<34)
print (not(price>10 and price<35))



temperature=14

if temperature>20:
    print("It's a hot day")
    print("drink a lot of water")
elif temperature>15:
    print("It's a nice chill day")
elif temperature>=15:
    print("it's a cold day")
else:
    print("get your coat")
print("Done")