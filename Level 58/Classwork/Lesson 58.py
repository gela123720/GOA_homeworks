def split_clone(text):
    result = []
    word = ""
    
    for words in text:
        if words == " ":
            if word != "":
                result.append(word)
                word = ""
        else:
            word += words
    
    if word != "":
        result.append(word)
    
    return result

print(split_clone("my name is gela"))
