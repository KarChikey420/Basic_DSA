def rev_sentence(sentence):
    word=sentence.split()
    result=[]
    
    for i in range(len(word)-1,-1,-1):
        result.append(word[i])
    return " ".join(result)

print(rev_sentence("i love python"))