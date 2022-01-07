# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None):
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        cp_dummy = dummy
        
        current = head
        
        start = False
        
        while (current.next != None):
            if (start == False and current.val != current.next.val):
                dummy.next = current
                dummy = dummy.next
                start = False
            elif (current.val == current.next.val):
                start = True
            elif (current.val != current.next.val):
                start = False
            #print(dummy)

                
            prev = current.val
            current = current.next
            
            
        if (prev == current.val):
            dummy.next = None
            
        else:
            
            dummy.next = current
            
        
            
            
            
            
        return cp_dummy.next
        
