class Queue:
    def __init__(self):
        self.values=[]
        self.front=-1
        
    def push(self, value):
        if self.front==-1:
            self.front=0
        return self.values.append(value)
        
    def pop(self):
       if self.front==-1:
           return None
       x=self.values[self.front]
       self.front+=1
       if self.front>=len(self.values):
           self.front=-1
           self.values=[]
       return x
    
    def peek(self):
        if not self.values:
            return None
        return self.values[self.front]
    
    def print(self):
        print(self.values)

if __name__=="__main__":
    queue=Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.print()
    print(queue.pop())
    print("Top element:", queue.peek())
