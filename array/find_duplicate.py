#find the duplicate in the list

# def find_duplicate(arr):
#     seen=set()
#     for num in arr:
#         if num in seen:
#             return num
#         seen.add(num)
#     return None

# arr=[1,4,3,2,5,4]
# print(find_duplicate(arr))

#second approach

# def duplicate(array):
#     duplicates = []
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             if array[i] == array[j]:
#                 duplicates.append(array[i])
#     return duplicates

# print(duplicate([2, 2, 3,3, 4, 5]))

#remove duplicates

# def remove_duplicate(arr):
#     result=[]
    
#     for item in arr:
#         if item not in result:
#             result.append(item)
#     return result
# arr=[1,2,1,3,2,4]               
# print(remove_duplicate(arr))

# def removed_dupli(arr):
#     k=1
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[i-1]:
#             arr[k]=arr[i]
#             k+=1
#         return k
    
# arr=[1,2,1,3,2,4]
# k=removed_dupli(arr)
# print(arr[:k])

def find_duplicate(arr):
    arr.sort()
    rm_list=[]
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            rm_list.append(arr[i])
    return rm_list
arr=[1,2,1,3,2,4]
print(find_duplicate(arr))