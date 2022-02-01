# Sliding Window Approach က Ngrams ဘာညာတွက်တဲ့နေရာ ပေါင်းတဲ့နေရာတွေမှာ အသုံးဝင်မယ် ထင်တယ်။



# 1. Naive Approach, Time Complexity - O(n-k+1) # by me
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = 0
        
        for i in range (len(nums)-k+1):
            avg =  sum(nums[i:i+k])/k
            print(nums[i:i+k])
            print(avg)
            if (i == 0):
                max_avg = avg
            if (avg > max_avg):
                max_avg = avg
        return max_avg


