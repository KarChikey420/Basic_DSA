def sort_asc(dictionary):
    sort_dict=sorted(dictionary.items())
    return dict(sort_dict)

def sort_desc(dictionary):
    sort_dict=sorted(dictionary.items(),reverse=True)
    return dict(sort_dict)
    
my_dict={1:"banana",
         3:"apple",
         2:"kiwi"}
print(sort_asc(my_dict))
print(sort_desc(my_dict))