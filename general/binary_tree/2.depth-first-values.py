                            a
                         b     c
                       d   e   f
      
  values: a,b, d,e , c, f
    
# ဒါလေးကို လိုက်ရေးကြည့်ပါ။ Left ဘက် သွားပြီးမှ Right ဘက်ကိုလာသာ။ Index တွေနဲ့ မှတ်ဖို့ စဉ်းစားနေရင် သေချာပြီ ရှုပ်ကုန်မှာ။ ခနခန ပြန်ရေးကြည့်နေ။

#1. Iterative Process, Time Complexity - O(n), Space Complexity - O(n)
# stack ပေါ် တင်ပြီး အလုပ်လုပ်တာ။
class Node:
    
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def depth_first_search_value(self, root):
        
        stack   = [root]
        values = []
        
        while (stack):
            
            val = stack.pop()
            print(val.val)
            values.append(val.val)
            
            if (val.right != None):
                print('Here')
                stack.append(val.right)
                print(stack)
                
            if (val.left != None):
                stack.append(val.left)
                print(stack)
        return values
                
                
                
a = Node ('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.left = b
a.right = c
b.right = d
print(a.depth_first_search_value (a))
            
