def find_palindrom(str1):
    str2=''
    for i in str1:
        str2=i+str2
        
    if str1==str2:
        return True
    else:
        return False
    
str1=input("Enter a string:")
if find_palindrom(str1):
    print("the given string is palindrom")
else:
    print("the given string is not palindrom")