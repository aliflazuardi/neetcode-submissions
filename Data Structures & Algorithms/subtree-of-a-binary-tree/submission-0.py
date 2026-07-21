# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if self.isIdentical(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False

    def isIdentical(self, node, subNode):
        if not node and not subNode:
            return True
        if not node or not subNode:
            return False
        if node.val != subNode.val:
            return False
        
        return self.isIdentical(node.left, subNode.left) and self.isIdentical(node.right, subNode.right)