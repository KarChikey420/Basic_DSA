def flatten(arr):
    result=[]
    
    for i in arr:
        if isinstance(i,list):
            result.extend(i)
        else:
            result.append(i)
    
    result.sort()
    return result

print(flatten([1,2,3,[2,5],[2,9,8]]))