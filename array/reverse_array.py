def reversing_arr(arr):
    left=0
    right=len(arr)-1
    
    for _ in range(1,len(arr)-1):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

print(reversing_arr([1,2,3,4,5]))