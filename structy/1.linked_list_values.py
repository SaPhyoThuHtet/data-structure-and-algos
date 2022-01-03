# Approach 1 (Time Complexity: O(n), Space Complexity: O(1) )
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
def linked_list_values(head):
  values = []
  current = head
  while (current != None):
    values.append(current.val)
    current = current.next
    
  return values

# Approach 2
