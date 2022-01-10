#Dict Approach (Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dic = {}
        for i in range(len(numbers)):
            if (target - numbers[i] not in dic):
                dic[numbers[i]] = i+1
            else:
                return [dic[target-numbers[i]], i+1]
              
              
             
            
# Two Pointer Approach (Time Complexity: O(n), Space Complexity: O(1) )
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(numbers) - 1
        
        while (start < end):
            add = numbers[start] + numbers[end]
            if ( add == target):
                return (start+1, end+1)
            elif (add < target):
                start +=1
            else:
                end -= 1
                
