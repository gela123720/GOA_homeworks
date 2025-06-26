name = []
result = []

for i in range(5):
    name_input = input("please enter a name: ")
    name.append(name_input)

vowels = "aeiou"

for j in name:
    for char in j:
        if char not in vowels:
            result.append(char)

print(sorted(set(result)))