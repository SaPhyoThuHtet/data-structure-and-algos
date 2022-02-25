class Node:
    
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None

    def bread_first_search_values(self, root):
    
        queue = [root]
        values = []
    
        while(queue):
            val = queue.pop(0)
            print(val.val)
            values.append(val.val)
        
        
            if (val.left != None):
                queue.append(val.left)
            
            if (val.right != None):
                queue.append(val.right)
            
        return values
    
    
a = Node ('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.left = b
a.right = c
b.right = d
print(a.bread_first_search_values(a))
            
