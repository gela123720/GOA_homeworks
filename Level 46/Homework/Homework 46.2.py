def list(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max

print(list([15 , 20 , 9 , 92]))