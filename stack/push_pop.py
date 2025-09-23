class Stack:
    def __init__(self):
        self.values=[]
        
    def push(self,value):
        self.values=[value]+self.values
        return self.values
    
    def pop(self):
        self.values=self.values.pop(0)
        return self.values
    
    def display(self):
        return self.values

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.display())
s.pop()
print(s.display())
