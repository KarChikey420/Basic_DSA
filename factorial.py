# def facto(num):
#     fact=1
#     if num==0 and num==1:
#         return 1
    
#     for i in range(1,num+1):
#         fact*=i
        
#     return fact

# print(facto(5))


# def fact(num):
#     fact=1
#     if num==0 and num==1:
#         return num
    
    
#     for i in range(1,num+1):
#         fact*=i
#     return fact
# print(fact(5))

def fact(num):
    if num == 0 or num == 1:  
        return 1
    else:
        return num * fact(num - 1)

print(fact(5)) 