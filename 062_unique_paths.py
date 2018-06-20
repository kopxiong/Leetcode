# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

import numpy as np

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # base case
        if m > 100 or n > 100:
            return
        if m == 1 or n == 1:
            return 1
        if m == 2 and n == 2:
            return 2
        # create a m x n matrix to store the paths
        path_list = [[0]*n for i in range(m)]
        for i in range(0, m):
            path_list[i][0] = 1
        for j in range(0, n):
            path_list[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                path_list[i][j] = path_list[i-1][j] + path_list[i][j-1]

        return path_list[m-1][n-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(10, 10))
