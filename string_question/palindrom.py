def palindrom(str1):
    reverse=""
    for i in str1:
        reverse=i+reverse
    
    if str1==reverse:
        return True
    else:
        return False

def isPalindrome(s):
        char = "".join(c.lower() for c in s if c.isalnum())
        n=len(char)
        l=0
        r=n-1

        while l<r:
            if char[l]!=char[r]:
               return False
            l+=1
            r-=1
        return True

str1="lebel"
if palindrom(str1):
    print("Palindrom")
else:
    print("Not Palindrom")