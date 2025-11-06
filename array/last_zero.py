def move_zero(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr

print(move_zero([0,0,1,2,4,5]))