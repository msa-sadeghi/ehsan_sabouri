name = input("enter a name:> ")
new_name = ""
for i in range(len(name)):
    if i == len(name) // 2:
        new_name += name[i].upper()
    else:
        new_name += name[i]
print(new_name)