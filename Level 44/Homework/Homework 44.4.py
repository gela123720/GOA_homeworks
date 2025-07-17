def num(list):
    sum = 0
    for i in list:
        sum = sum + i
    print(sum / len(list))

num([5 , 10 , 23 , 52])