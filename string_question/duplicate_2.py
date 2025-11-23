def findTheDifference(s, t) :
        freq_str={}
        for i in s:
            freq_str[i]=freq_str.get(i,0)+1

        for i in t:
            if freq_str.get(i,0)==0:
               return i
            freq_str[i]-=1
print(findTheDifference("abcd","abcde"))
         