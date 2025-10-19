def reverse(str1):
    rev=''
    for i in str1:
        rev=i+rev
    return rev

print(reverse("hello world"))