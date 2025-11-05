def flatten_list(arr):
    arr1=[]
    for i in arr:
        if isinstance(i,list):
            arr1.extend(flatten_list(i))
        else:
            arr1.append(i)
    return arr1

print(flatten_list([1,2,[1,2],[3,4],8,9]))