class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            ans = max(ans, profit)

            if prices[l + 1] < prices[l]:
                l += 1
                if l == r:
                    r += 1
            else:
                r += 1
        
        while l < r:
            profit = prices[r-1] - prices[l]
            ans = max(ans, profit)
            l += 1


        return ans