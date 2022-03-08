# Time Limited Exceeded Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if strs == [""]:
            return [[""]]
        
        if (len(strs) == 0 or len(strs) == 1):
            return strs
        
        
        
        ans = []
        
        dic = []
        
        for i in range(len(strs)):
            if sorted(strs[i]) not in dic:
                dic.append(sorted(strs[i]))
                
                ans_part = [strs[i]]
                for j in range (i+1, len(strs)):
                    if (sorted(strs[i]) == sorted (strs[j]) ):
                        ans_part.append(strs[j])
                        
                        
                ans.append (ans_part)
                
        return ans
                
        
        
        
