def min_max(arr):
    min=arr[0]
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
           max=arr[i]
        else:
            min=arr[i]
    return max,min
print(min_max([1,2,3,4,5]))