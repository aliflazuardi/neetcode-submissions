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
private:
    int dfs(TreeNode* node, int len, bool& isBalanced) {
        if (node == nullptr){
            return len;
        }       
        
        int left = dfs(node->left, len+1, isBalanced);
        int right = dfs(node->right, len+1, isBalanced);
        int diff = abs(left - right);
        isBalanced = isBalanced && (diff <= 1);
        return max(left, right);
    }

public:
    bool isBalanced(TreeNode* root) {
        bool isBalanced = true;
        dfs(root, 0, isBalanced);

        return isBalanced;
    }
};
