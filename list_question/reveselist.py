#using the empty list
list1=[2,3,4,5,6]
list2=[]

for i in list1:
    list2.insert(0,i)
    
print(list2)

#using slicing

list1=[2,3,4,5,6]
print(list1[::-1])

#using reverse function

list1=[2,3,4,5,6]
list1.reverse()
print(list2)

#using reversed function

list1=[2,3,4,5,6]
list2=list(reversed(list1))
print(list2)
