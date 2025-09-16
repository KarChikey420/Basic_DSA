def selection_sort(array):
    n=len(array)
    for i in range(n):
        min_index=i
        for j in range(j+1,n):
            if array[j]>array[min_index]:
                min_index=j
                array[i],array[min_index]=array[min_index],array[i]
    return array

array=[6,7,4,5,2,3,1]
arr=selection_sort(array)
print(arr)