// Given a binary tree, find its maximum depth.
// The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
// Note: A leaf is a node with no children.

#include <iostream>
#include <queue>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // 1. DFS:
        // if (!root) {
        //     return 0;
        // }
        // int leftHeight=0, rightHeight=0;
        // if (root->left) {
        //     leftHeight = maxDepth(root->left);
        // }
        // if (root->right) {}
        //     rightHeight = maxDepth(root->right);
        // }
        //
        // return std::max(leftHeight, rightHeight) + 1;

        // return root == NULL ? 0 : std::max(maxDepth(root->left), maxDepth(root->right)) + 1;

        // 2. BFS:
        if (root == NULL)
            return 0;

        int result = 0;
        std::queue<TreeNode *> q;
        q.push(root);
        while (!q.empty())
        {
            ++result;
            // q is the sibling node in the tree
            for (int i = 0, n = q.size(); i < n; ++i)
            {
                TreeNode *p = q.front();
                q.pop();

                if (p -> left != NULL)
                    q.push(p -> left);
                if (p -> right != NULL)
                    q.push(p -> right);
            }
        }

        return result;
    }
};

int main() {
    Solution Test;
    struct TreeNode *root = new TreeNode(1);
    root->left            = new TreeNode(2);
    root->right           = new TreeNode(3);
    root->left->left      = new TreeNode(4);
    root->left->right     = new TreeNode(5);

    std::cout << "Max Depth: " << Test.maxDepth(root) << std::endl;
}
