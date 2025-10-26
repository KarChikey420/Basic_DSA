def febbo(n):
    feb=[0,1]
    for i in range(2,n):
        feb.append(feb[i-1]+feb[i-2])
    return feb
print(febbo(10))