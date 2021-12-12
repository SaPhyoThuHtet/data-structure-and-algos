#1st Idea 1 မဖြစ်ရင် Count တာကို 0 လုပ်ပြီး သွားမယ်ဆိုပြီး စဉ်းစားမိတယ်။  ဒါပေမယ့် ခု လို cases မျိုးကျ အဆင်မပြေဘူး။ End မှာက 0 မပါလို့"
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        count_one = 0
        
        for i in nums:
            if (i == 1):
                count_one +=1
            else:
                if(count_one>max_num):
                    max_num = count_one
                count_one = 0
        return max_num
Ans: [1,1,0,1,1,1], Program's Answer => 2, Expected=> 3
'''

# First Idea ရဲ့ လိုအပ်ချက်ကို ပြင်ပြီး ခုလိုရေးလိုက်တယ်။ Time Complexity (O(n)), Space Complexity (O(1))
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.append(0)
        
        max_num = 0
        count_one = 0
        
        for i in nums:
            if (i == 1):
                count_one +=1
            else:
                if(count_one>max_num):
                    max_num = count_one
                count_one = 0
                
        return max_num
"""
