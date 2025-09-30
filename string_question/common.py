str1='neena'
str2='reena'
str3=''
for i in str1:
    for i in str2:
        if i not in str3 and i in str1 and i in str2:
            str3+=i

print(str3)