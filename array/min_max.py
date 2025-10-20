def min_max(arr):
    min=arr[0]
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    return max,min
arr=[1,2,3,4,5]
print(min_max(arr))