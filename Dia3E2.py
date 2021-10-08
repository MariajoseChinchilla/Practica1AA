class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        minbuy = prices[0]
        maxprofit = 0

        for price in prices[1::]:
            maxprofit = max(maxprofit,price-minbuy)
            minbuy = min(minbuy, price)
        return maxprofit