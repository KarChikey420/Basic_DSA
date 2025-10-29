def febbonici(num):
    feb=[0,1]
    for i in range(2,num):
        feb.append(feb[i-1]+feb[i-2])
    return feb

num=int(input("Enter the num:"))
print(febbonici(num))