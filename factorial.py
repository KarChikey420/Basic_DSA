def fact(num):
    result=1
    for i in range (1,num+1):
       result*=i
       
    return result
    
num=int(input("enter the number:"))
print(fact(num))