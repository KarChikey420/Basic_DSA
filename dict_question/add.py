from collections import Counter
# def add(dict1,dict2):
#     combined_dict=dict1.copy()
    
#     for key , value in dict2.items():
#         if key in combined_dict:
#             combined_dict[key]+=value
#         else:
#             combined_dict[key]=value
            
#     return combined_dict

# print(add({"a": 100, "b": 200}, {"a": 300, "c": 400}))

dict1={"a": 100, "b": 200}
dict2={"a": 300, "c": 400}

dict3=dict(Counter(dict1)+Counter(dict2))
print(dict3)