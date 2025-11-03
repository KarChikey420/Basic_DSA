from collections import Counter

def are_anagrams(str1,str2):
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)
    
    if sorted_str1==sorted_str2:
        return True
    else:
        return False

if __name__=="__main__":
    string1="listen"
    string2="silent"
    
    result=are_anagrams(string1,string2)
    if result:
        print(f"{string1} and {string2} are anagrams")
    else:
        print(f"{string1} and {string2} are not anagrams")
        