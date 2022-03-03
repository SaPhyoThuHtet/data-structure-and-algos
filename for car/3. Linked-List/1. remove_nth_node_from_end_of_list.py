Idea 1
# ၁ ခု ဆိုရင် Node.next == None နဲ့သွားမယ်
# ၂ ခုဆိုရင် Node.next.next = None နဲ့သွားမယ်  Etc စဥ်းစားမိတယ်။ But Code ရေးဖို့က မပြေ

# Hint
Maintain two pointers and update one with a delay of n steps.
ဒီကောင်ကို ဘယ်လိုလုပ်ရမလဲ စဥ်းစားရ ခက်နေတယ် #ဒါကိုတော့ Video ကြည့်မယ်။
Video ကိုကြည့်လိုက်တယ်။ Intuitive ဖြစ်စွာတော့ နားမလည်ဘူး။ ဒါပေမယ့် ဒီ Approach က တော်တော် အသုံးဝင်တယ်ဆိုတာ သိတယ် ဘယ်လို လုပ်လဲကြည့်ရအောင်။
Video သာ ကြည့်လိုက်ပြီး Trace လိုက်ပေါ့။

# Idea 2
ကျိန်းသေပေါက်ရမယ့် Approach တစ်ခု ကတော့ Linked List ကို Array လို့ သဘောထားတယ်။ 
Elements အရေအတွက်ကို Count လုပ်မယ်။ ပြီးရင် သူ့နံပါတ်ရောက်ရင် Process လုပ် ဒါပဲ။


# ခုCode မှာ ရလိုက်တာတွေကတော့ အများကြီးပဲ။ Dummy.next ကို Return ပြန်တာရော။
# Visualization က အရေးကြီးတယ် ဆိုတာကော နောက်ဆုံးnth node ကို သိဖို့ရာ ခုလို Concept ကလည်းပဲ တော်တော် အသုံးဝင်တယ် ဆိုတာကိုရော သိလိုက်ရတယ်။

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        slow = dummy
        fast = head
        
        while (n>0):
            fast = fast.next
            n -=1
            
        
        while (fast): # Until fast reaches the end of the list
            slow = slow.next
            fast = fast.next
            
            
        slow.next = slow.next.next
        
        return dummy.next
        
        
