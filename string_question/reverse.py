#using empty string 

char="python"
char1=""

for i in char:
    char1=i+char1
    
print(char1)

#using slicing 

char="python"
char1=char[::-1]
print(char1)