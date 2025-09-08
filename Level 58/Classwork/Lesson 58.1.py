def join_clone(thing1, thing2):
    result = ""
    which = True
    for i in thing2:
        i = str(i)
        if which:
            result += i
            which = False
        else:
            result += thing1 + i
    return result

words = ["Hello", "World", "Python"]
print(join_clone(" ", words))
