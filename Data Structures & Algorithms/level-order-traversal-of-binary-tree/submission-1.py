# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        curr_level = 0
        queue = deque([(root, curr_level)])

        ans = []
        level_nodes = []

        while queue:
            node, level = queue.popleft()
            if level != curr_level:
                ans.append(level_nodes)
                curr_level = level
                level_nodes = []
            
            level_nodes.append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        ans.append(level_nodes)

        return ans