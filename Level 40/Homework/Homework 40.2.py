sentence = input("please enter a sentence: ")
space = ""

for i in sentence:
    if i == i.upper():
        space += i.lower()
        space = space.capitalize()

print(space)