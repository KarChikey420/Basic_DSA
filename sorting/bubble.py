def bubble_sort(arr):
    for i in range(len(arr)):
      for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
          temp=arr[i]
          arr[i]=arr[j]
          arr[j]=temp
          
    return arr
          
array=[4,3,5,6,2,1]
arr=bubble_sort(array)
print(arr)