def flatten(list1):
    flat_list=[]
    for i in list1:
        if isinstance(i,list):
            flat_list.extend(flatten(i))
        else:
            flat_list.append(i)
    return flat_list
print(flatten([1,2,[3,4],[5,[6,7]],8]))