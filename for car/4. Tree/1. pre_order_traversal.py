Link: https://www.hackerrank.com/challenges/tree-preorder-traversal/
 

#Iterative Approach: Time Complexity O(n), Space Complexity O(n)
def preOrder(root):
    #Write your code here
    stack = [root]
    
    while(stack):
        val = stack.pop()
        print(val.info, end =" ")
        if(val.right):
            stack.append(val.right)
        if(val.left):
            stack.append(val.left)
            

# Recursion Approach: Time Complexity O(n), Space Complexity: O(n)
    def preOrder(root):
    values = recursion(root)
    
    for i in values:
        print(i, end = " ")
    
def recursion(root):
    if (root == None):
        return []
    
    return [root.info]+recursion(root.left)+recursion(root.right)
  
  
  
  
            
