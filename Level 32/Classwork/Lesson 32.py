names = ["gela" , "sandro" , "giorgi"]

number = int(input("Please enter any number from 0 to 2: "))

while number < 0 or number > 2:
    print("incorrect input! ")
    number = int(input(("Please enter any number from 0 to 2: ")))


print(names[number])