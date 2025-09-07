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