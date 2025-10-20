def check_array(arr):
    ascending=True
    descending=True
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            ascending=False
        elif arr[i]>arr[i-1]:
            descending=False
    if ascending:
        return("array is sorted in ascending")
    elif descending:
        return("array is sorted in descending")
    else:
        return("array is not sorted")

arr1=[1,2,3,4,5]
arr2=[5,4,3,2,1]

print(check_array(arr1))
print(check_array(arr2))
