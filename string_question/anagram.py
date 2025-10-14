from collections import Counter

def anagram(str1,str2):
    sort_str1=sorted(str1)
    sort_str2=sorted(str2)
    
    if Counter(sort_str1)==Counter(sort_str2):
        return True
    else:
        return False
    
print(anagram('abc','cba'))