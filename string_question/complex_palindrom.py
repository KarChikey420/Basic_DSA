def isPalindrome(s) -> bool:
    char = "".join(c.lower() for c in s if c.isalnum())
    n=len(char)
    i=0
    j=n-1

    while i<j:
        if char[i]!=char[j]:
            return False
        i+=1
        j-=1
    return True
