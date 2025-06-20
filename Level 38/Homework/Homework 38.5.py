list = []

for i in range(3):
    students = input("please enter a students name: ")
    list.append(students)
    
list.insert(0 , "Nika")
list.pop(2)
print(len(list))
print(list)
