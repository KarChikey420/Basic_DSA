# Square numbers dictionary
# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
# Expected: {1:1, 2:4, 3:9, 4:16, 5:25}

dictionary={x:x**2 for x in range(1,6)}
print(dictionary)