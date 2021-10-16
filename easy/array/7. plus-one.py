class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = 0
        length_of_digits = len(digits)
        for i in range(len(digits)):
            num += digits[i]*(10**(length_of_digits-1))
            length_of_digits -=1
            
        return [int(i) for i in str(num+1)]
            
