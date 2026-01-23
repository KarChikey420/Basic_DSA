class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
        
    def enqueue(self,value):
        newnode=Node(value)
        if self.front is None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
        self.size+=1
    
    def dequeue(self):
        if self.front is None:
            return None
        
        x=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        self.size-=1
        return x
    
    def peek(self):
        if self.front is None:
            return None
        
        return self.front.data
    
    def printlink(self):
        x=self.front
        while x:
            print(x.data,end='->')
            x=x.next
        print("None")

if __name__=="__main__":
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue:")
    queue.printlink()
    
    dequeued=queue.dequeue()
    print(f"Dequeued: {dequeued}")
    print("After dequeue:")
    queue.printlink()
    
    print("Front element:", queue.peek())