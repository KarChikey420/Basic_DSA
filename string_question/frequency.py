def get_freq(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

print(get_freq("aaabbbccc"))