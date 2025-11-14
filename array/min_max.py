def min_max(arr):
    min=arr[0]
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
        elif arr[i]>max:
            max=arr[i]
    return max,min
print(min_max([1,2,3,4,5]))