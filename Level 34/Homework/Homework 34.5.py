#7) შექმენით 5 ელემენტიანი სია. გამოიყენეთ for ციკლი, range და len ფუნქციები, რომ შეცვალოთ ამ სიაში არსებული ყოველი მეორე ელემენტი თქვენი სახელით. შემდეგ დაბეჭდეთ ეს სია.

animals = ["dog" , "cat" , "horse" , "cow" , "pig"]

name = "gela"

result = ""

for i in range(len(animals)):
    if i % 2 == 0:
        result += name + " "
    else:
        result += animals[i] + " "

print(result)