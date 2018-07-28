# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).

from collections import deque

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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            level_ans = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level_ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.insert(0, level_ans)

        return result

if __name__ == '__main__':
    root = TreeNode([3, 9, 20, None, None, 15, 7])

    print(Solution().levelOrderBottom(root))
