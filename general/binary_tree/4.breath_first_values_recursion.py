# ပထမဦးဆုံးတုန်းက Base case ကို Empty ဖြစ်ရင် ဆိုပြီး စဥ်းစားတယ်။ 
နောက် leaf node ဖြစ်နေရင် Base case က ပိုမှန်တယ်ဆိုတာကို သဘောပေါက်လာတယ်။

Error တွေ့တာကတော့ def ပြန်ခေါ်တဲ့နေရာမှာ self တွေကျန်ခဲ့တာ Detail Oriented ဖြစ်ဖို့လိုတယ်။
နောက်တော့ code မှာ current val + left+ right တွေ တစ်ခါတည်း ပြန်မိတယ်။ But Eg right child မရှိရင် None ဖြစ်နေတော့ None ရဲ့ left တွေ right တွေရှာရင် Error တက်တယ်။

အထင်။ ။ Time Complexity (O(n)), Space Complexity O(n)
class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
    def depth_first_values_recursion(self, node):
        
        if (node.left == None and node.right == None):
            return node.val
            
        else:
            ans = [node.val]
            if (node.left != None):
                l = self.depth_first_values_recursion(node.left)
                ans += list(l)
            if (node.right != None):
                r = self.depth_first_values_recursion(node.right)
                ans += list(r)
            
            return ans
                
            
            
            
            
            
            
            
            
            
            
a = Node ('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.left = b
a.right = c
b.right = d


print(a.depth_first_values_recursion(a))
