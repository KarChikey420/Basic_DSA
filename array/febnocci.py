def febbo(num):
    feb=[0,1]
    for i in range(2,num):
        feb.append(feb[i-1]+feb[i-2])
    return feb

print(febbo(10))

# def febbnocci(num):
#     a,b=0,1
#     for _ in range(num):
#         yield a
#         a,b=b,a+b
        
# for num in febbnocci(10):
#     print(num)