class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None            
        
a = Node("A")
b = Node("B")
c = Node("C")

a.next = b
b.next = c


def traverse(head):
        current = head
        while current != None:
            print(current.val)
            current = current.next
            
traverse(a)
