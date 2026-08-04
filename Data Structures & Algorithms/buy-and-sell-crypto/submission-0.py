class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        res = 0
        n = len(prices)
        while i < n and j < n:
            net = prices[j] - prices[i]
            if net <= 0:
                i = j
                j = i + 1
            else:
                res = max(res, net)
                j += 1
        
        return res
        