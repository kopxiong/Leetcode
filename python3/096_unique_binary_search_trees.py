# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

import numpy as np

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        # more efficient
        # nums = [1]
        # for a in range(1, n+1):
        #     nums.append(sum([nums[i] * nums[a-i-1] for i in range(a)]))
        #
        # return nums[n]

        nums = [0] * (n+1)
        nums[0] = 1

        # store all the numbers for [1, n]
        for i in range(1, n+1):
            for j in range(i):
                nums[i] += nums[j] * nums[i-j-1]

        return nums[n]

if __name__ == '__main__':
    n = 4

    print(Solution().numTrees(n))
