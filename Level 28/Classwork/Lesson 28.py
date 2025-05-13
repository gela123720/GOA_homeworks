age = int(input("Please Enter your age: "))

if age < 18:
    if age < 14:
        print("discount 20%")
    else:
        print("discount 10%")

elif age >= 18:
    print("no discount")

