def remove_duplicate(list1:list):
    list2=[]
    for i in list1:
        if i not in list2:
           list2.append(i)
    return list2

print(remove_duplicate([1,2,1,3,2,4,5]))