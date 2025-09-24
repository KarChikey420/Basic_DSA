def max_key(dictionary):
    max_value=max(dictionary.values())
    for key, value in dictionary.items():
        if value==max_value:
            return key
        
print(max_key({"a": 100, "b": 200, "c": 50}))