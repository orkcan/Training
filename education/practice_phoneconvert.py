phone= input("Enter your Phone:")
dictionary_of_phone= {
        "1" : "One",
        "2" : "Two",
        "3" : "Three",
        "4" : "Four",
        "5" : "Five",
        "6" : "Six",
        "7" : "Seven",
        "8" : "Eight",
        "9": "Nine",
        "0" : "Zero"
        }
output=""
for char in phone:
    output += (dictionary_of_phone.get(char,"!")+(" "))
print(output)



#print(customer.get("birthdate","Jan 2 1993")) #default value added for this "key"
#print(customer.get("y"))

        #customer[1] : "One",
         #customer[2] : "Two",
        #customer[3] : "Three",
        #customer[4] : "Four",
        #customer[5] : "Five",
        #
        #customer[7] : "Seven",
        #customer[8] : "Eight",
        #customer[9] : "Nine",
       # customer[0] : "Zero"