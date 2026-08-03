# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])
        left = min(p.val, q.val)
        right = max(p.val, q.val)

        while queue:
            node = queue.popleft()

            if node.val >= left and node.val <= right:
                return node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return root 