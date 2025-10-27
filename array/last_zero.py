def zero_last(arr):
   j=0
   for i in range(len(arr)):
       if arr[i]!=0:
           arr[i],arr[j]=arr[j],arr[i]
           j+=1
   return arr
    
print(zero_last([1,0,2,0,3,0,4,0]))