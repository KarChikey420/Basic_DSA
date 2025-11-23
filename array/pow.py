def myPow(x, n):
        sqrt=1
        power=abs(n)
        for _ in range(power):
            sqrt*=x
        
        if n<0:
            return 1/sqrt
        return sqrt
print(myPow(2.00000, -2))  