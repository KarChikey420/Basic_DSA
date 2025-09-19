def flatten(nested_list):
    result=[]
    for i in nested_list:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

nested = [[1, 2], [3, [4, 5]], 6]
print(flatten(nested))