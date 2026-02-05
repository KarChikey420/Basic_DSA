def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called")
        value=func(*args, **kwargs)
        print("Something is happening after the function is called")
        return value
    return wrapper

@my_decorator
def add_numbers(a,b):
    return a+b

print(add_numbers(5,3))
