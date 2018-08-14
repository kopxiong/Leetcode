# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).

# Time complexity: O(n), single pass
# Space complextiy: O(1), constant space needed

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        diff = [prices[i+1] - prices[i] for i in range(len(prices)-1)]

        return sum([d if d > 0 else 0 for d in diff])

        """
        maxprofit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                maxprofit += prices[i+1] - prices[i]

        return maxprofit
        """

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]

    print(Solution().maxProfit(prices))
