def reverse(str):
    reverse_str=''
    
    for i in str:
        reverse_str=i+reverse_str
    return reverse_str

str=input("Enter a stirng: ")
print("reversed string is:",reverse(str))