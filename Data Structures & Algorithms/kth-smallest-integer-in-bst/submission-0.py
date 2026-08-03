# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    ans = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k

        self.dfs(root)
        return self.ans

    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return 

        self.dfs(node.left)
        if self.count == 0:
            return 
        self.count -= 1
        if self.count == 0:
            self.ans = node.val
        self.dfs(node.right)

