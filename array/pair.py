def all_pair(arr,target):
    pair=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                pair.append((arr[i],arr[j]))
    return pair
    
print(all_pair([1, 2, 3, 4, 5], 6))
