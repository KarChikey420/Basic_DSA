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
print(twoSum([2,7,11,15],9))