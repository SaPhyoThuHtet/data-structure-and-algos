class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        current = head

        while current !=None:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
            
            #print("Here", current)
        #print(prev)    
        return prev
