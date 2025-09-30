def count_freq():
    str1=input("enter the sentance:")
    list1=str1.split()
    freq={}
    
    for i in list1:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq)
    
count_freq()