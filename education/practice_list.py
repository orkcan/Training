numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7]
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)


#second approach

list1=[1,1,2,2,3,3,4,4,5,5,6,6,7]
list2=[]
for number in list1:
    if number not in list2:
        list2.append(number)
print(list2)