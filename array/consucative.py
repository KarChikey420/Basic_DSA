# def consecutive(arr):
#     list1=[]
#     for i in range(len(arr)-1):
#         current=arr[i]
#         next=arr[i+1]
#         for n in range(current+1,next):
#             list1.append(n)
#     return list1

# print(consecutive([1,3,5,7]))

def consecutive(arr):
    for i in range(len(arr)-1):
        if arr[i+1]!=arr[i]+1:
            return arr[i]+1

print(consecutive([1,2,4,6,7,8]))