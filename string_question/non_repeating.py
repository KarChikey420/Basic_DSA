def non_repeating(str1):
    dict1={}
    
    for i in str1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    
    for i,val in dict1.items():
        if val<=1:
            return i
print(non_repeating("aabbcddee"))