def sum_avg(arr):
    addition=0
    avg=0
    
    for i in range(len(arr)):
        addition+=arr[i]
        
    avg=addition/len(arr)
    return addition,avg

arr=[1,2,3,4]
print(sum_avg(arr))