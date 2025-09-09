list1=[2,3,4,5,2,5]
duplicates=list({x for x in list1 if list1.count(x)>1})
print(duplicates)