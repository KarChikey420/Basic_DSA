num=10
feb=[0,1]

for i in range(2,num):
    feb.append(feb[i-1]+feb[i-2])
    
print(feb)