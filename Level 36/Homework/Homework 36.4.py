word = input("please enter some words: ")
symbol = input("please enter a symbol: ")
count = 0

for i in word:
    if i == symbol:
        count += 1

print(count)