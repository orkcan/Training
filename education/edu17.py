#tuples

numbers=(1,2,3,4)
numbers.count(3)
numbers.index(3)


#unpacking

coordinates=(1,2,3)
coordinates[0]*coordinates[1]*coordinates[2]
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]
x*y*z

coordinates=[2,3,4]   #works for lists and tuples as well
x, y, z = coordinates
coor2=coordinates.copy()
print(coor2)
