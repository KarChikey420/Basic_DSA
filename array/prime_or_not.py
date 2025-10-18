def prime_or_not(num):
    if num<=1:
        return False
    
    for i in range(2,num):
        if num%i==0:
            return False
            
    return True

for i in range(0,100):
    if prime_or_not(i):
        print(f"{i} is prime")