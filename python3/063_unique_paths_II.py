# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

import numpy as np

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # create a m x n matrix to store the paths
        path_list = [[0]*n for _ in range(m)]
        path_list[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    path_list[i][j] = 0
                else:
                    if i-1 >= 0:
                        path_list[i][j] += path_list[i-1][j]
                    if j-1 >= 0:
                        path_list[i][j] += path_list[i][j-1]

        return path_list[-1][-1]

if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
