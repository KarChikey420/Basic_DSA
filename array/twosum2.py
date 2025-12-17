def twoSum(numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            s=numbers[i]+numbers[j]

            if s<target:
                i+=1
            elif s>target:
                j-=1
            else:
                return [i+1,j+1]

def two_sum(arr,target):
    mapp={}
    for i,n in enumerate(arr):
        diff=target-n
        if diff in mapp:
            return [mapp[diff],i]
        mapp[n]=i
        
print(twoSum([2,7,11,15],9))