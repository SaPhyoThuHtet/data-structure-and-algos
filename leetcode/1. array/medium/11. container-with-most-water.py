""" ဒီproblem က မိုက်တယ် ရိုးရိုး naive approach နဲ့ သွားလို့ရပေမယ့် Time Complexity က များတယ်။ Left Index နဲ့ Right Index ကို ထားပြီး Two pointer  approach နဲ့ ဖြေရှင်းတဲ့အခါ Time Complexity က O(n) ပဲ ရှိတော့တယ်။"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        left_index = 0
        right_index = len(height)-1
        count = 0
        
        while (left_index < right_index and count < len(height)):
            current_area = min(height[left_index], height[right_index]) * (right_index-left_index)
            max_area = max(max_area, current_area)
            
            
            if(height[left_index] < height[right_index]):
                left_index +=1
                
            else:
                right_index -= 1
                
            count +=1
            
        return max_area 
