def singleNumber(nums):
    count={}
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
        
    for key,value in count.items():
        if value==1:
            return key
 
print(singleNumber([4,1,2,1,2]))       
        