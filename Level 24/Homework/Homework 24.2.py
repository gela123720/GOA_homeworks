secret = 5
tries = 3
user_number = int(input("please enter a number: "))

while user_number != secret:
    while tries >= 0:
        tries -= 1
        print("wrong number! " + str(tries) + " left")
        user_number = int(input("please enter another number: "))
        if tries == 1:
            print("you lost!")
            break
    break

if user_number == secret:
    print("you win!")



