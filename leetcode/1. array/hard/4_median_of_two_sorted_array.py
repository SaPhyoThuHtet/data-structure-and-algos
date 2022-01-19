# ဒီမှာတော့ Merge Sort ကို သုံးပြီး ဖြေရှင်းထားတာ။ Merge Sort ကတော့ Time Complexity O(nlogn) ရှိတယ်။ ဒီ့ထက်ပိုကောင်းအောင်တော့ ရေးလို့ရသေးတယ်။

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = nums1+nums2
        nums = self.merge_sort(nums)
        #print(nums)
        if (len(nums)%2 == 0):
            index = int(len(nums)/2)
            #print(index)
            #print(nums[index-1])
            #print(nums[index])
            return ((nums[index-1]+nums[index])/2)
        
        else:
            index = int(len(nums)/2)
            return (nums[index])
        
    def merge_sort(self, nums):
        if (len(nums) < 2):
            return nums
        
        medium = len(nums)//2
        
        
        return self.merge(self.merge_sort(nums[0:medium]), self.merge_sort(nums[medium:]))
    
    
    def merge (self, left_arr, right_arr):
        results = []
        l_index = 0
        r_index = 0
        #print("L",left_arr)
        #print("R", right_arr)
    
        while (l_index < len(left_arr) and r_index < len(right_arr)): #ဒီနားလွဲတတ်လို့ သတိထားပါ။
            if (left_arr[l_index] < right_arr[r_index]):
                results.append(left_arr[l_index])
                l_index += 1
                
            elif (left_arr[l_index] == right_arr[r_index]):
                results.append(left_arr[l_index])
                results.append(right_arr[r_index])
                l_index += 1
                r_index += 1
                
            else:
                results.append(right_arr[r_index])
                r_index += 1
                
           
                
        if l_index != len(left_arr):
            results += left_arr[l_index:]
            
        if r_index != len(right_arr):
            results += right_arr[r_index:]
            
        return results
    
        
