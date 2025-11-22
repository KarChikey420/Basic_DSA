def removeDuplicates(nums):
        n=len(nums)
        j=0

        for i in range(1,n):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]

        return j+1