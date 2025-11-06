def max_subarray(arr):
    max_current=arr[0]
    max_globle=arr[0]
    
    for i in range(1,len(arr)):
        max_current=max(arr[i],max_current+arr[i])
        max_globle=max(max_globle,max_current)
    return max_globle

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))