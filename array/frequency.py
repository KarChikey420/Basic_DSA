def frequency(list1):
    freq={}
    for i in list1:
        if i not in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
print(frequency([1,3,2,1,2,4,5,5]))