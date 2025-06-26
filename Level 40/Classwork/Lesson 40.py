sentence = input("Enter a sentence: ")

result = ""

is_space = False

for i in sentence.lower():
    if i == " ":
        is_space = True
    elif is_space:
        result += i.upper()
        is_space = False
    else:
        result += i
print(result)