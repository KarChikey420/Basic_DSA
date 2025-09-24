class Queue:
    def __init__(self,values):
        self.values=values
        
    def enqueue(self,value):
        self.values.append(value)
        return self.values
        
    def dequeue(self):
        return self.values.pop(0)
    
    def is_empty(self):
        return len(self.values)==0
    
    def display(self):
        return self.values
    
    def peek(self):
        return self.values[0]
    
q=Queue([1,2,3,4,5])
q.enqueue(6)
print(q.display())
q.dequeue()
print(q.display())
print(q.peek())