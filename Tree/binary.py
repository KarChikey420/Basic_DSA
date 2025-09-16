class Node:
    def __init__(self,value,left,right):
        self.value=value
        self.left=None
        self.right=None
        
class Binary_Tree:
    def __init__(self):
        self.root=None
        
    def insert(self,value):
        if not self.root:
            self.root=value
        else:
            self._insert(self.root,value)
    
    def insert(self,current,value):
         
    

    