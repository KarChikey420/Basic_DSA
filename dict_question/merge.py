# Merge two dictionaries:
# Merge d1 = {"a": 1, "b": 2} and d2 = {"c": 3, "d": 4} into one.

d1={"a": 1, "b": 2}
d2={"c": 3, "d": 4}

d1.update(d2)
print(d1)