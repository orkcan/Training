def find_max(numbers):
    max= numbers[0]
    for number in numbers:
        if number >max:
            max = number
    print(max)
    return max
