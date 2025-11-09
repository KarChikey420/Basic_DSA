def palindrom(str1):
    reverse=""
    for i in str1:
        reverse=i+reverse
    
    if str1==reverse:
        return True
    else:
        return False

str1="lebel"
if palindrom(str1):
    print("Palindrom")
else:
    print("Not Palindrom")