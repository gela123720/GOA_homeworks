#ფუნქცია არის კოდის ბლოკი, რომელიც მხოლოდ მისი გამოძახებისას მუშაობს.
#ფუნქციაში შეგიძლიათ გადასცეთ მონაცემები, რომლებიც პარამეტრების სახელითაა ცნობილი.
#შედეგად, ფუნქციას შეუძლია მონაცემების დაბრუნება.

first = int(input("Please enter your first number: "))
second = int(input("Please enter your second number: "))
operator = input("Please enter your symbol (+ , - , * , / , // , %): ")

def calculator(x , y , op):
    if type(x) == int and type(y) == int:
        if op == "+":
            return x + y
        
        elif op == "-":
            return x - y
        
        elif op == "*":
            return x * y
        
        elif op == "/":
            return x / y
        
        elif op == "//":
            return x // y
        
        elif op == "%":
            return x % y
        
        else:
            print("invalid input!")

    else:
        print("invalid value!")

print(calculator(first , second , operator))