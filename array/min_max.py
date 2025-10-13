def min_max(arr):
    min=0
    max=0
    
    for i in range(1,len(arr)):
        if arr[i]<arr[min]:
            min=i
        elif arr[i]>arr[max]:
            max=i
    return min,max

print(min_max([2,3,5,6,8,9]))
        