numbers=[1,2,3,4,5,6,7,8,9]
print(numbers[0])
numbers[0]=10
print(numbers[0])
print(numbers[-1])

print(numbers[0:3])



numbers.append(6)
print(numbers)
numbers.insert(-1,-1)
print(numbers)

numbers.remove(-1)
print(numbers)

print(10 in numbers)  #boolean
print(len(numbers))
numbers.clear()
print(numbers)
