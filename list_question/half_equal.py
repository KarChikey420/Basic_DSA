def divide_half_equal(list1):
    mid=len(list1)//2
    first_half=list1[:mid]
    second_half=list1[mid:]
    
    return first_half,second_half

print(divide_half_equal([1,2,4,6,7,7,8,8,9]))
