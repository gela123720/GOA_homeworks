print("please enter your exam score:")

score = int(input())

if score > 80:
    print("you got an A!")

elif score > 60:
    print("you got a B!")

elif score > 40:
    print("you got a C")

elif score > 20:
    print("you got a D..")

elif score < 20:
    print("you got an F...")


print("you got " + str(score) + " out of a 100")