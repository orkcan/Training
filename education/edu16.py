numbers = [11,21,3,4,5,3,3]
numbers.insert(0,2)
print(numbers)

print(numbers.index(4)) or print(4 in numbers)  #boolean
numbers.remove(5)

numbers.pop()   #removes the last
print(numbers)
# numbers.clear()
print(numbers.index(11))   #returns the first index of 11
print(numbers)
print(numbers.count(3))   #returns the count of the number
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.append(10)
print(numbers)
print(numbers2)