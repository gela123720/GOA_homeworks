positive_num = 0
negative_num = 0

for i in range(5):
    num = int(input("Please enter a number: "))

    if num > 0:
        positive_num = positive_num + 1
    elif num < 0:
        negative_num = negative_num + 1

print("Positive numbers count: " + str(positive_num))
print("Negative numbers count: " + str(negative_num))