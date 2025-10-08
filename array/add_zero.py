def add_zero(nums):
    n=len(nums)
    
    for i  in range(n-1,-1,-1):
        if nums[i]<9:
            nums[i]+=1
        return nums
    
    return [1]+[0]*n

print(add_zero([1,2,3]))