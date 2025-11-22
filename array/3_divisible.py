def minimumOperations(nums):
    count=0
    n=len(nums)

    for i in range(n):
        if nums[i]%3!=0:
            count+=1
    return count

nums=[4,3,6,7,9,10]
print(minimumOperations(nums))