def recursive_fact(num):
    if num==1:
        return 1
    else:
        return num*recursive_fact(num-1)
    
print(recursive_fact(5))