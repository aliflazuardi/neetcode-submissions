# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s_p = deque()
        s_q = deque()
        if p:
            s_p.append(p)
        if q:
            s_q.append(q)

        while s_p and s_q:
            p_n = s_p.pop()
            q_n = s_q.pop()

            if p_n.val != q_n.val:
                return False
            
            if ((p_n.left is not None) ^ (q_n.left is not None)) or ((p_n.right is not None) ^ (q_n.right is not None)):
                return False
            
            if p_n.left and q_n.left:
                s_p.append(p_n.left)
                s_q.append(q_n.left)
            if p_n.right and q_n.right:
                s_p.append(p_n.right)
                s_q.append(q_n.right)
        
        if s_p or s_q:
            return False

        return True 