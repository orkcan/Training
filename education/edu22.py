while True:
    try:
        age = int(input('Enter your age: '))
        income = 20000
        risk = income / age
        print(age)
    except ZeroDivisionError:
        print('Age can not be zero if you are not an integer.')
    except ValueError:
        print('Invalid value')
    except KeyboardInterrupt:
        print("no no no")
#ValueError: invalid literal for int() with base 10: 'asd'
#Process finished with exit code 1            this is the error for string entry
#try except
#ZeroDivisionError: division by zero this is for entry of 0. should be another except

