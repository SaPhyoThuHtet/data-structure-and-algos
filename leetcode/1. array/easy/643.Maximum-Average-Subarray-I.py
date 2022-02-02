# Sliding Window Approach က Ngrams ဘာညာတွက်တဲ့နေရာ ပေါင်းတဲ့နေရာတွေမှာ အသုံးဝင်မယ် ထင်တယ်။



# 1. Naive Approach, Time Complexity -  O((n-k+1)*k) #by me
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

# 2. Naive Approach, max_avg = float('-inf')

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        
        for i in range (len(nums)-k+1):
            avg =  sum(nums[i:i+k])/k
            print(nums[i:i+k])
            print(avg)
            if (avg > max_avg):
                max_avg = avg
        return max_avg

    
 # 3. Sliding Window Approach (Prev ဆိုတဲ့ စကားလုံးကြောင့်ရှုပ်နေမလားတော့ မသိဘူး) ဒီ approach တော်တော်မိုက်တယ်။ 
# 1 2 3 4, k = 2 ဆိုပါစို့
# ပထမ တစ်ခေါက် အတွက် ကတော့ 1+2 = 3ကိုloop ပတ်ပေါင်းမယ်။ (k=10 ဆို index ၁၀ ခုစာ loopပတ်ရမှာ )
# ဒုတိယ အခေါက်ကျ Loop ပတ်ပေါင်း စရာ မလိုတော့ဘူး။ (3(ခုန ပေါင်းထားတဲ့ တန်ဖိုး)-1(ပထမဆုံး index: ခုက နှစ်ကနေ စမှာဆိုတော့ 1 မပါတော့ ပြန်နှုတ်တာ) +4 (ခုအသစ်ဝင်လာတဲ့ တန်ဖိုး))
# ခုပုံစံ Sliding Window Approach ကို n-gram လိုမျိုး တွက်တဲ့ နေရာမှာ(ပေါင်းတဲ့ နေရာမှာ) သုံးရင် အသုံးတည့်မယ် လို့ထင်တယ်။ တော်တော် efficient ဖြစ်မှာ။
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_val = float('-inf')
        start_val = nums[0]
        prev = 0
        
        for i in range (0, len(nums)-k+1):
            
            if (i != 0):
                prev = (prev-start_val)+nums[i+k-1]
                start_val = nums[i]
                if ((prev/k) > max_val):
                    max_val = (prev/k)
            
            else:
                prev = sum(nums[i:i+k])
                max_val = prev/k
                
        return max_val
                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
