def consecutive(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i+1]!=arr[i]+1:
            return arr[i]+1
        # if i+1 not in arr:
        #     return i
    return "all elements are consecutive"

arr=[1,2,3,5,6]
print(consecutive(arr))
