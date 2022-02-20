#Approach 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
        
        for i in set_nums:
            if (nums.count(i) == 1):
                return i
            
            
            
# Approach 2           (Sorted စီပြီးသွားတယ်Codeကနည်းနည်းတော့ပိုရှုပ်လာတယ်)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1 2 2 3 3 1 
        
        sorted_nums = sorted(nums)
        index = 0
        
         #1 1 2 3 3
        while (index < len(sorted_nums)-1):
            print(index)
            if(sorted_nums[index] == sorted_nums[index+1]):
                index += 2
            else:
                return sorted_nums[index]
            
        if (len(sorted_nums)>1): # အထူးသဖြင့် ဒီနေရာ Len( 1) နဲ့ More than Len(1) Case
            if (sorted_nums[-1] != sorted_nums[-2]):
                return sorted_nums[-1] 
        
        else: #if (len(sorted_nums) == 1):
                return sorted_nums[0]    
            
        
        
        
            
            
            
        
        
