def check_consucative(arr):
    missing=[]
    
    for i in range(len(arr)-1):
        current=arr[i]
        next_val=arr[i+1]
        if current+1!=next_val:
            for num in range(current+1,next_val):
                   missing.append(num)
    return missing
    
print(check_consucative([1,2,4,6,8]))