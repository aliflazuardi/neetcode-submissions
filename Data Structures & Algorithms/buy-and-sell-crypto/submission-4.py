class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minBuy = prices[0]

        for price in prices:
            ans = max(ans, price - minBuy)
            minBuy = min(minBuy, price)


        return ans 