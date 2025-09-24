def invert(dictionary):
    invert_dict={}
    for key , value in dictionary.items():
        invert_dict[value]=key
        
    return invert_dict

print(invert({1:"a",2:"b"}))