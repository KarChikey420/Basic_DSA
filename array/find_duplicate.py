# def duplicate(arr):
#     arr.sort()
#     dupli=[arr[0]]
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[i-1]:
#             dupli.append(arr[i])
#     return dupli
    
# print(duplicate([1,2,4,5,2,1,4]))

def duplicate(arr):
    arr.sort()
    dupli=[]
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            dupli.append(arr[i])
    return dupli
    
print(duplicate([1,2,4,5,2,1,4]))