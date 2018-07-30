# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            return "[{}, {}, {}]".format(self.val, repr(self.left), repr(self.right))

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if not t1:
            return t2
        if not t2:
            return t1

        t1.val = t1.val + t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


if __name__ == "__main__":
    t1 = TreeNode([1, 3, 2, 5])
    t2 = TreeNode([2, 1, 3, None, 4, None, 7])

    print(Solution().mergeTrees(t1, t2))
