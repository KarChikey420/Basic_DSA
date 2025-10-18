def min_max(arr):
    min=arr[0]
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    return max,min

print(min_max([1,2,4,6,7]))