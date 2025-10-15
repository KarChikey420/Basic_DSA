def consecutive(arr):
    list1=[]
    for i in range(len(arr)-1):
        current=arr[i]
        next=arr[i+1]
        for n in range(current+1,next):
            list1.append(n)
    return list1

print(consecutive([1,3,5,7]))