def two_sum_problem(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return [i,j]

print(two_sum_problem([1,7,9,11],10))
