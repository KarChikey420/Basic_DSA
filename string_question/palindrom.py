def palindrom(str1):
    str2=""
    for i in str1:
        str2=i+str2
    
    if str1==str2:
        return True
    else:
        return False

if __name__=="__main__":
    str1=input("Enter The String:")
    if palindrom(str1):
        print("Number is palindrom")
    else:
        print("Not a palindrom")