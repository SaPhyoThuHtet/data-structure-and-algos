# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (l1 == None and l2 == None):
            return None
        
        l1_list = self.append_to_list(l1)            
        l2_list = self.append_to_list(l2)
            
        l1l2 = sorted(l1_list+l2_list)[::-1]
        
        node = ListNode(l1l2[0], None)
        
        for i in l1l2[1:]:
            next_node = node
            node = ListNode(i, next_node)
            
        return node
    
    def append_to_list(self, l):
        l_list = []
        while(l!=None):
            l_list.append(l.val)
            l = l.next
            
        return l_list
        
        
