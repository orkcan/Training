names=['Joseph', 'George', 'Daniel', 'John', 'Sara']
print(names[2:4])
print(names[2:])
print(names)
names[1]= 'Georg'
print(names)




numbers=[1,2,3,4,15,6,7,8,22,10]
largest=max(numbers)
print(largest)

largest1=numbers[0]
for number in numbers:
    if number > largest1:
        largest1 = number
print(largest1)