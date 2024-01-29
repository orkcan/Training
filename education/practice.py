weight=float(input("Enter your weight:"))
unit=input("(K)g or (L)bs:")
if unit=="K" or unit=="k":
    result="lbs"
    converted=str(weight/0.45)
    print("Weight in " + result + ":" + converted)
elif unit=="L" or unit=="l":
    result="kg"
    converted = str(weight * 0.45)
    print("Weight in " + result + ":" + converted)

#print("Weight in " + result + ":"+str(weight))155