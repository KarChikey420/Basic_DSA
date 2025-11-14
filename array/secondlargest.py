def second_largest(arr):
   first=second=0
   
   for i in range(len(arr)):
      if arr[i]>first:
         second=first
         first=arr[i]
      elif arr[i]>second and arr[i]!=first:
         second=arr[i]
   return second

print(second_largest([1,2,3,4,5]))
         