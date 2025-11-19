def lengthOfLastWord(s):
    word=s.split()
    return len(word[-1])
print(lengthOfLastWord("Hello World"))  