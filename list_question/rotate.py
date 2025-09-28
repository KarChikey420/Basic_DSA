def rotate_list(lst, k):
    k = k % len(lst)
    for _ in range(k):
        last = lst.pop()  
        lst.insert(0, last) 
    return lst

arr = [1, 2, 3, 4, 5]
print(rotate_list(arr, 2))  
