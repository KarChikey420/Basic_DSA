def prime_or_not(num):
  if num<=1:
      return False
  
  for i in range(2,num):
      if num%i==0:
        return False
    
  if num%num==0:
     return True
   
print(prime_or_not(1))
    