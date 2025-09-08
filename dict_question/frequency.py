# Count frequency of elements in a list
# Given a list ["apple", "banana", "apple", "orange", "banana", "apple"], create a dictionary that counts how many times each fruit appears.
# Expected: {"apple":3, "banana":2, "orange":1}

list1=["apple", "banana", "apple", "orange", "banana", "apple"]
frequency={}

for i in list1:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
        
print(frequency)