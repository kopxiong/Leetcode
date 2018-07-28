# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps.
# You need to find minimum cost to reach the top of the floor,
# and you can either start from the step with index 0, or the step with index 1.

# Dynamic programming algorithm: time complexity: O(N), space complexity: O(1), in-place

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        cur = pre = 0
        for x in cost:  # for x in cost[::-1]:
            cur, pre = x + min(cur, pre), cur

        return min(cur, pre)


if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    print(Solution().minCostClimbingStairs(cost))
