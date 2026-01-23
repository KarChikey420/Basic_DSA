class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
        self.size=0
        
    def push(self,value):
        newnode=Node(value)
        newnode.next=self.top
        self.top=newnode
        self.size+=1
            
    def pop(self):
        if self.top is None:
            return None
        data=self.top.data
        self.top=self.top.next
        self.size-=1
        return data
    
    def peek(self):
        if self.top is None:
            return -1
        
        return self.top.data
    
    def printlink(self):
        current=self.top
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
            
if __name__=="__main__":
    stack=Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack:")
    stack.printlink()
    
    popped=stack.pop()
    print(f"Popped: {popped}")
    print("After pop:")
    stack.printlink()
    
    print("Top element:", stack.peek())
    