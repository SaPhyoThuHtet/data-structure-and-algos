I Think : Time Complexity (O(nlogn)), Space Complexity: O(1)
Time: 32 mins

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes = [[i[1],i[0]] for i in boxTypes]
        boxTypes = sorted(boxTypes)[::-1]
        boxTypes = [[i[1],i[0]] for i in boxTypes]
        
        ans      = 0
        index    = 0
        
        print(boxTypes)
        while (truckSize>0 and index<len(boxTypes)):
            
            if (truckSize-boxTypes[index][0]>=0):
                ans       += boxTypes[index][0]*boxTypes[index][1]
                truckSize -= boxTypes[index][0]
            else:
                ans += truckSize*boxTypes[index][1]
                truckSize = 0
                
            index +=1
            
        return ans
            
        
    
