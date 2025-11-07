def max_sub_arr(arr):
    current_max=arr[0]
    global_max=arr[0]
    
    for i in range(1,len(arr)):
         current_max=max(arr[i],current_max+arr[i])  
         global_max=max(global_max,current_max)
        
print(max_sub_arr([-2, 1, -3, 4, -1, 2, 1, -5, 4]))