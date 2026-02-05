try:
    value=int("kartik")
except ValueError:
    print("input is invailid")
else:
    print("value valid",value)
finally:
    print("execution completed")
