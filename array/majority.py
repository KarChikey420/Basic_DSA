def majorityElement(nums):
    majority={}
    for i in nums:
        if i in majority:
            majority[i]+=1
        else:
            majority[i]=1

    return max(majority,key=majority.get)

print(majorityElement([3,2,3]))