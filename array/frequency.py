def count_frequency(list1):
    list2={}
    for i in list1:
        if i in list2:
            list2[i]+=1
        else:
            list2[i]=1
    return list2
    
list1=[1,2,3,4,1,2,3]
print(count_frequency(list1))            