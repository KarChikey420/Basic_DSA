def list_to_dict(list1,list2):
    result={}
    
    for i in range(len(list1)):
        result[list1[i]]=list2[i]
    return result

list1=[1,2,3]
list2=["abc","def","ghk"]
print(list_to_dict(list1,list2))

        