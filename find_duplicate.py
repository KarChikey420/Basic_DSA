#find the duplicate in the list

def find_duplicate(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None

arr=[1,4,3,2,5,4]
print(find_duplicate(arr))

#second approach

def duplicate(array):
    duplicates = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                duplicates.append(array[i])
    return duplicates

print(duplicate([2, 2, 3,3, 4, 5]))
