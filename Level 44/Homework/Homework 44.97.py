def sentence(words):
    biggest = ""
    for word in words:
        if len(word) > len(biggest):
            biggest = word
    print(biggest)


sentence(["BMW" , "Lamborghini" , "Honda" , "Bugatti"])