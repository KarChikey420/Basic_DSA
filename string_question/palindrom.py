def palindrom(str1):
    rev_str=""
    for i in str1:
        rev_str=i+rev_str
    
    if rev_str==str1:
        return True
    else:
        return False

if __name__=="__main__":
    str1="ladal"
    if palindrom(str1):
        print("palindrom")
    else:
        print("not")