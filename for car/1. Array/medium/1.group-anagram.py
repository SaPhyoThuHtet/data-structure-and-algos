ကဲ Accepted ဖြစ်သွားတာက အောင်မြင်မှု တစ်ခုပါပဲ။ Congratulations. ရသွားတာက sort လုပ် dic မှာ မရှိရင် dic ထဲထည့်။ ရှိရင် အဲ့စကားလုံးရဲ့ Index ထဲမှာ ထပ်ထည့်။


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
                
        
        
# First Accepted Version
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if strs == [""]:
            return [[""]]
        
        if (len(strs) == 0 or len(strs) == 1):
            return strs
        
        
        
        ans = []
        
        dic = {}
        count = 0
        
        for i in range (len(strs)):
            #print(strs[i])
            sorted_str = ''.join(sorted(strs[i]))
            if (sorted_str not in dic):
                dic[sorted_str] = count
                count +=1
                ans.append([strs[i]])
                #print(ans)
                
            else:
                #print(dic)
                ans[dic[sorted_str]].append(strs[i])
                
        return ans
                
        
        
                
# Second Accepted Version        
        
        class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''if strs == [""]:
            return [[""]]
        
        if (len(strs) == 0 or len(strs) == 1):
            return strs'''
        
        
        
        ans = []
        
        dic = {}
        count = 0
        
        for i in range (len(strs)):
            #print(strs[i])
            sorted_str = ''.join(sorted(strs[i]))
            if (sorted_str not in dic):
                dic[sorted_str] = count
                count +=1
                ans.append([strs[i]])
                #print(ans)
                
            else:
                #print(dic)
                ans[dic[sorted_str]].append(strs[i])
                
        return ans
                
        
        
                
        
        
        
