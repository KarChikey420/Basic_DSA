def flatten_list(list1):
    flatten=[]
    for i in list1:
        if isinstance(i,list):
            flatten.extend(flatten_list(i))
        else:
            flatten.append(i)
    return flatten

print(flatten_list([1,2,[1,3],[3,4]]))