def flatten_list(list1):
    list2=[]
    for i in list1:
        if isinstance(i,list):
            list2.extend(flatten_list(i))
        else:
            list2.append(i)
    return list2
    
print(flatten_list([1,2,[3,4],[5,[6,7]],8]))