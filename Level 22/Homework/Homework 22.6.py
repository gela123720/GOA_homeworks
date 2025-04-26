year = int(input("please enter a year: "))

if year % 4 == 0 and year % 400 != 0:
    print("this is a leap year")

elif year % 100 == 0:
    print("this is not a leap year")