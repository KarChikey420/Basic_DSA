class Stack:
    def __init__(self):
        self.values=[]
    
    def push(self, value):
        return self.values.append(value)
        
    def pop(self):
       if not self.values:
           return None
       return self.values.pop()
    
    def peek(self):
        if not self.values:
            return None
        return self.values[-1]
    
    def print(self):
        print(self.values)

if __name__=="__main__":
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print()
    
    stack.pop()
    stack.print()
    print("Top element:", stack.peek())
    stack.print()
   
    