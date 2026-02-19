def generator(num):
    i=0
    j=1
    for _ in range(1,num):
        yield i
        i,j=i,i+j

