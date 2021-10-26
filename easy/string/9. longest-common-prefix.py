class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      """
      Input: strs = ["flower","flow","flight"]
      Output: "fl"
      
     
      """
        ans = ""
        
        s = strs[0] #flower
        min_length = min([len(i) for i in strs]) #To get min length and avoid index out of bound error
        
        for i in range(min_length): #use min_length
            for j in strs[1:]: # starting from the second index of the array
                if (s[i] not in j[i]): #first: f in all of the index of the array, #second l in all of the index of the array ... If not return ans
                    return ans 
            ans += s[i]# if s[i] in all of the index of the array, it will add to the ans, first: ""+"f", second: "f"+"l" etc
                    
        return ans
