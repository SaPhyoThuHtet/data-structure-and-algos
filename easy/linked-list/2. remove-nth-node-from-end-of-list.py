# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        len_list = 0
        while node != None:
            len_list += 1
            node = node.next
            
        if (len_list-n == 0): # for the case like [1]n=1, [1,2]n= 2
            return head.next
        
        node2 = head
        index =1 
        while (index < len_list-n):
            node2 = node2.next
            index = index+1
    
        node2.next = node2.next.next
        
        return head
