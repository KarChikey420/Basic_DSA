# def check_consacutive(arr):
#     missing=[]
    
#     for i in range(len(arr)-1):
#         current=arr[i]
#         next_val=arr[i+1]
        
#         if current+1!=next_val:
#             for num in range(current+1,next_val):
#                 missing.append(num)
#     return missing
    
# arr=[1,3,5,7]
# print(check_consacutive(arr))

def check_consacutive(arr):
    for i in range(len(arr)-1):
        current=arr[i]
        next_val=arr[i+1]
        
        if current+1!=next_val:
            return current+1
            
arr=[1,3,4,5]
print(check_consacutive(arr))