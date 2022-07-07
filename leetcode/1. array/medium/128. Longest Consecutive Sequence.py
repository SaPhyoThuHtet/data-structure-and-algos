Time Complexity O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxi = 0
        nums_set = set(nums)
        for i in range (len(nums)):
            
            if nums[i]+1 not in nums_set:
                val = nums[i]-1
                count = 1
                while (val in nums_set):
                    count +=1
                    val = val-1
                print(nums[i], count)
                if (count>maxi):
                    maxi = count
        return maxi
        
