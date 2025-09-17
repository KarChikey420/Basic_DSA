def facto(num):
    fact=1
    if num==0 and num==1:
        return 1
    
    for i in range(1,num+1):
        fact*=i
        
    return fact

print(facto(5))