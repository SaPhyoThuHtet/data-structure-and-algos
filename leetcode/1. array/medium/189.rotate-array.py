# Rotate Array:  ဒီ problem ကို မြင်တာနဲ့ reverse လှန်ရမယ်ဆိုတာ သိနေတယ်။ I think it is a kind of improvement. But do not try to memorize. Please Generalize 


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        print(nums)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        
        return nums
        
    def reverse (self, nums, start, end):
        
        start = start
        end = end
        
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            
            start += 1
            end -= 1
            
        
        
