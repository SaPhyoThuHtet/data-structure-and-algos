Sorting စီတယ် နှစ်ခါ နှစ်ခါသွားတယ်။ တူနေရင် index ကို 2 တိုးတယ်။ မဟုတ်ရင် index ကို 1 တိုးတယ်။

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        index = 0
        ans = []
        nums = sorted(nums)
        while (index <= len(nums)-2):
            
            if (nums[index] == nums[index+1]):
                ans.append(nums[index])
                index += 2
            else:
                index +=1
                
        return ans
                
                
        
