def get_freq(str1):
    freq_dict={}
    for i in str1:
        if i in freq_dict:
            freq_dict[i]+=1
        else:
            freq_dict[i]=1
    return freq_dict

if __name__=="__main__":
    string="programming"
    frequency=get_freq(string)
    print(f"Character frequency in '{string}': {frequency}")