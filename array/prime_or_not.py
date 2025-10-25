def prime_or_not(num):
    if num<=1:
        return False 
    for i in range(2,num):
        if num%i==0:
           return False
    return True

num=int(input("Enter a number")) 
if prime_or_not(num):
    print("prime number")
else:
    print("not a prime number")