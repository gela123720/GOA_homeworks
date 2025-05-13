symbol = input("please enter a symbol (+ , - , * , / , // or %): ")
number1 = float(input("please enter the first number: "))
number2 = float(input("please enter the second number: "))

if symbol != "+" and symbol != "-" and symbol != "*" and symbol != "/" and symbol != "//" and symbol != "%":
    print("invalid symbol! choose another one")

if symbol == "/" or symbol == "//" or symbol == "%" or number1 == 0 or number2 == 0:
    print("cant divide by zero")

if symbol == "+":
    print(number1 + number2)

elif symbol == "-":
    print(number1 - number2)

elif symbol == "*":
    print(number1 * number2)

elif symbol == "/" and number1 != 0 and number2 != 0:
    print(number1 / number2)

elif symbol == "//" and number1 != 0 and number2 != 0:
    print(number1 // number2)

elif symbol == "%" and number1 != 0 and number2 != 0:
    print(number1 % number2)




