def devide_half(arr):
    mid=len(arr)//2
    first_half=arr[mid:]
    second_half=arr[:mid]
    return first_half,second_half

print(devide_half([1,2,3,4,5,6,7,8,9,10]))