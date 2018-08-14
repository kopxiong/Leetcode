# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

class Solution:

    # need extra space
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     if len(prices) == 0 or len(prices) == 1:
    #         return 0
    #
    #     profits = [0] * len(prices)
    #     for i in range(len(prices)-1):
    #         if (prices[i] < prices[i+1]):
    #             profits[i] = max(prices[i+1:]) - prices[i]
    #
    #     return max(profits)

    # def maxProfit1(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     temp, max_profit = 0, 0
    #
    #     for i in range(len(prices)-1):
    #         temp += prices[i+1] - prices[i]
    #         if temp < 0:
    #             temp = 0
    #         elif temp > max_profit:
    #             max_profit = temp
    #
    #     return max_profit

    # Dynamic programming
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0

        minPrice, maxProfit = prices[0], 0
        for i in range(len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i]-minPrice)

        return maxProfit


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [1, 2]

    print(Solution().maxProfit1(prices))
