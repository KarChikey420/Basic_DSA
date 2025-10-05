def facto(num):
    if num==1:
        return 1
    else:
        return num*(facto(num-1))
    #fact=1
    # for i in range(1,num+1):
    #     fact*=i
    # return fact

print(facto(5))