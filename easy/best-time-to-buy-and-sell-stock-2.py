class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        buy = prices[0]
        sell, maxprofit = 0, 0
    
        while i < len(prices)-1:
            indicator = False #important
            while (i<len(prices)-1 and prices[i+1] <= prices[i]): # di nay yar mhar [i+1] ka greater than equal (not i)
                i = i+1
                buy = prices[i]
                print("buy", buy)
               
            
            while(i<len(prices)-1 and prices[i+1] >= prices[i]):
                i = i+1
                sell = prices[i]
                indicator = True # for the case like the value of the last array is smaller than the previous one and (sell-buy) but buy is an old one[,,,,4]
            
            if(indicator):
                maxprofit += sell-buy
            
        return maxprofit
    
