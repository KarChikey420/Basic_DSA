def merge_arr(arr1,arr2):
    merge=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merge.append(arr1[i])
            i=i+1
        else:
            merge.append(arr2[j])
            j=j+1
            
    merge.extend(arr1[i:])
    merge.extend(arr2[j:])
    return merge

print(merge_arr([1,3,5],[2,4,6]))