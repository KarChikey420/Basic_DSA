def most_common(list1):
    freq = {}
    for i in list1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    max_count=max(freq.values())
    for key, value in freq.items():
        if value==max_count:
            return key
            
print(most_common([1, 2, 2, 3, 4, 2, 5, 3, 3]))
