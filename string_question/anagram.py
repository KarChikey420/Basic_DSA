from collections import Counter
def anagram(str1,str2):
    sort_str1=Counter(str1)
    sort_str2=Counter(str2)
    
    if sort_str1==sort_str2:
        print("anagrams")
    else:
        print("not a anagram")
    
        
str1="listen"
str2="silent"
anagram(str1,str2)