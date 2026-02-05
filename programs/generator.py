arr=[1,2,3,4,5,6]

def my_generator(array):
    i,j=0,1
    for _ in range(1,len(array)-1):
        yield i
        i,j=j,i+j
        
print(list(my_generator(arr)))