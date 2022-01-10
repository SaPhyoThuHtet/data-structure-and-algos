class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums = sorted(nums)
        results = []
        
        for i in range(0, len(nums)-2):
            self.twoSum(nums, i, results)
            
        return results
    
    def twoSum(self, nums, i, results):
        target = 0-nums[i]
        dic = {}
        #print(dic)
        #print()
        #print(dic)
        for j in range(i+1,len(nums)):
            diff = target-nums[j]
            #print("Target",target)
            #print(diff)
           # print(dic)
           # print(diff)
            
            if (diff not in dic):
                #print("Here")
            
                dic[nums[j]] = True
                
            elif (diff in dic):
                r = [nums[i], diff, nums[j]]
                if  r not in results:
                    results.append(r)
            
                
            
