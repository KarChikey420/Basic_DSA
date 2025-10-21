def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return "no index"
print(linear_search([1,2,3,4],2))