# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

from __future__ import print_function
import numpy as np

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recursive solution
class Solution:
    def _generateTrees(self, nums):
        if not nums:
            yield None
        for i in range(len(nums)):
            for left in self._generateTrees(nums[:i]):
                for right in self._generateTrees(nums[i+1:]):
                    root = TreeNode(nums[i])
                    root.left = left
                    root.right = right
                    yield root

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return list(self._generateTrees(range(1, n+1)))

'''
class Solution1:
    def __init__(self):
        self.memo = {}

    # generate key for map
    def genKey(self, m, n):
        return (m, n)

    def genTreesRange(self, start, stop):
        if stop == start:
            return [None]
        key = self.genKey(start, stop)
        if key in self.memo:
            return self.memo[key]
        r = self.memo[key] = []
        for i in range(start, stop):
            left = self.genTreesRange(start, i)
            right= self.genTreesRange(i + 1, stop)
            for leftTree in left:
                for rightTree in right:
                    node = TreeNode(i)
                    node.left = leftTree
                    node.right = rightTree
                    r.append(node)
        return r

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTreesRange(1, n + 1)
'''

if __name__ == '__main__':
    results = Solution().generateTrees(3)

    print(results)
