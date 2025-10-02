def generator_function(num):
    for i in range(1,num+1):
        if i%2==0:
            yield i

print(list(generator_function(10)))