def read_generate(limit):
    num=0
    while num<=limit:
        if num % 2==0:
            yield num
        num+=1
        
for value in read_generate(10):
    print(value)

    