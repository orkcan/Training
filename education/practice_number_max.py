# we defined a function in utils.py called find_max()
nums = [10, 3, 5, 2]

from utils import find_max
find_max(nums)

# max=find_max(nums)  #owerwrites the built in function value which  is considered as bad programming
# print(max(nums))  #max is a int now since we changed it. TypeError: 'int' object is not callable


#rename the max to maximum

maximum = find_max(nums)
print(maximum)