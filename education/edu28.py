#check the module index in Python
#directories (path class from patlib(obj-oriented filesys paths module)

#we can use absolute path:we start from the root of our HDD,
# relative path : starting from current directory,
#c:\Program Files\Microsoft
# /usr/local/bin
from pathlib import Path   #P is capital(class)
directory=Path("ecommerce")
directory2=Path("newdir_test")
directory3=Path("emails")   #creates emails since it's not existent
# print(directory.exists())  # returns True
# print(directory.mkdir(ecommerce2.joinpath(directory)))
# print(directory.mkdir())   # you can't create an existing folder
# print(directory3.mkdir())
# print(directory3.rmdir()) #returns None but it's deleted
# print(directory2.rmdir())
dir4=Path()
print(dir4.glob('*.*'))     #glob method searches for files in current dir
# * would mean to search for all files and directories, *.* only brings files
# not the directories
print(dir4.glob('*.py'))
print(dir4.glob('*.xls'))

#The glob method returns a generator,
# and you need to iterate over it to see the results.
# output is "<generator object Path.glob at 0x000002044BC65360>"
#The value "0x000002044BC65360" is a
# hexadecimal representation of a memory address,

# for file in dir4.glob('*.py'):
#     print(file)   #iterated all *py file names over the
    # returned generator object

# for file in dir4.glob('*'):    #all  files and dirs
#     print(file)

for file in dir4.glob('*.*'): print(file)  # just files


