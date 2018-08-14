# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).

import math

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell1, buy1, sell2, buy2 = 0, -math.inf, 0, -math.inf
        for i in range(len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2


if __name__ == '__main__':
    prices = [1, 6, 3, 4, 5]

    print(Solution().maxProfit(prices))
