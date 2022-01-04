class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    
    
a = Node("a")
b = Node("b")
c = Node("c")

a.left = b
a.right = c
