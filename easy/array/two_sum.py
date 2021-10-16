class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        count = -1
        
        for i in nums:
            count = count+1
            
            if (target-i not in dictionary):
                dictionary[i] = count
            else:
                return(count, dictionary[target-i])
        
