sentence = input("Please enter a sentence: ")
space = 0

for i in sentence:
    if i == " ":
        space += 1
print("there are " + str(space) + " spaces in this sentence")
