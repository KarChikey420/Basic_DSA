# Dictionary methods practice:

# 1. Safe access with .get()
dict1 = {"name": "John", "age": 25, "city": "New York"}
print(dict1.get("country", "Not found"))

# 2. Get all keys, values, items
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# 3. Add new key-value pair
dict1["country"] = "USA"
print(dict1)

# 4. Update existing value
dict1["age"] = 26
print(dict1)

# 5. Remove item
del dict1["city"]
print(dict1)