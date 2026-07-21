/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root != nullptr) {
            swapChilds(root);
        }
        return root;
    }

    void swapChilds(TreeNode* node) {
        TreeNode* temp = node->left;
        node->left = node->right;
        node->right = temp;

        if (node->left != nullptr) {
            swapChilds(node->left);
        }

        if (node->right != nullptr) {
            swapChilds(node->right);
        }
    }
};
