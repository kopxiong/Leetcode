# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        ways = [0 for i in range(amount+1)]
        n = len(coins)

        for i in range(1, amount+1):
            smallest = float("inf")
            for j in range(0, n):
                if (coins[j] <= i):
                    smallest = min(smallest, ways[i-coins[j]])
            ways[i] = 1 + smallest

        if ways[amount] == float("inf"):
            ways[amount] = -1

        return ways[amount]


if __name__ == '__main__':
    coins = [2]
    amount = 3
    print(Solution().coinChange(coins, amount))
