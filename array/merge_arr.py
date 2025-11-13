def merge_array(arr1,arr2):
    merge_arr=[]
    i=0
    j=0
    while i<len(arr1)and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr1.append(i)
            i+=1
        else:
            arr2.append(j)
            j+=1
            
    if i<len(arr1):
        arr1.append(i)
        i+=1
    if j<len(arr2):
        arr2.append(j)
        j+=1
    
    return merge_arr

arr1=[1,2,3]
arr2=[3,4,5]

merged=merge_array(arr1,arr2)
print(merged)