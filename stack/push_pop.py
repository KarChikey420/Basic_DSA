class Stack:
    def __init__(self):
        self.values = []
        
    def push(self, value):
        self.values.append(value)
        return self.values
    
    def pop(self):
        if not self.values:
            return "Stack is empty"
        return self.values.pop()
    
    def display(self):
        return self.values


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.display())  

s.pop()
print(s.display()) 

s.push(4)
print(s.display()) 
