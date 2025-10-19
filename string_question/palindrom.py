def palindrom(str1):
    rev=''
    for i in str1:
        rev=i+rev
    
    if rev==str1:
        return True
    else:
        return False
    
print(palindrom("madam"))