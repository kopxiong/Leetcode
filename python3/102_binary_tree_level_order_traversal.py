# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __repr__(self):
    #     if self:
    #         return "[{}, {}, {}]".format(self.val, repr(self.left), repr(self.right))


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = [root]
        ans = []
        while queue:
            level_size = len(queue)
            level_ans = []
            for _ in range(level_size):
                node = queue.pop(0)
                level_ans.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ans.append(level_ans)

        return ans


if __name__ == '__main__':
    root = TreeNode([3, 9, 20, None, None, 15, 7])

    print(Solution().levelOrder(root))
