sentence = input("Please enter a sentence: ")
space = ""

for i in sentence:
    if i == " ":
        space += "_"
    else:
        space += i
print(space)