class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float("inf")
        maxprofit = 0
        for price in prices:
            minprice = min(price,minprice)
            profit = price-minprice
            maxprofit = max(profit,maxprofit)
        return maxprofit