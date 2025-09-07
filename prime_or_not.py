def prime_or_not(num):
    if num<=1: 
      return f"{num} not a prime number"
      
    for i in range(2,num):
        if num%i==0:
            return f"{num} not a prime number"
    
    return f"{num} is prime number"
    

num1=int(input("Enter a number: "))
print(prime_or_not(num1))