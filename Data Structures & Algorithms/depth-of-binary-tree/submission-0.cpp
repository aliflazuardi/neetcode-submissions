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
    stack<pair<TreeNode*, int>> nodes;
public:
    int maxDepth(TreeNode* root) {
        int depth = 0;
        if (root != NULL) {
            depth++;
            processNode(root, depth);
        }
        
        while(!nodes.empty()) {
            pair<TreeNode*, int> pair = nodes.top();
            nodes.pop();
            depth = max(depth, pair.second);
            processNode(pair.first, pair.second);
        }

        return depth;        
    }

    void processNode(TreeNode* node, int depth) {
        if (node->left != NULL) {
            nodes.push({node->left, depth+1});
        }
        if (node->right != NULL) {
            nodes.push({node->right, depth+1});
        }
    }
};
