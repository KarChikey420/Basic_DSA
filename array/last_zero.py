# def zero_last(arr):
#    j=0
#    for i in range(len(arr)):
#        if arr[i]!=0:
#            arr[i],arr[j]=arr[j],arr[i]
#            j+=1
#    return arr
    
# print(zero_last([1,0,2,0,3,0,4,0]))

def move_zero(arr):
    arr1=[]
    zero_count=0
    for i in arr:
        if i!=0:
            arr1.append(i)
        else:
            zero_count+=1
    arr1.extend([0]*zero_count)
    return arr1

print(move_zero([1,0,2,0,3,0]))