# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.is_equv = True
    
    def checkTree(self, p, q):

        if not p and not q:
            return

        if (not p and q) or (p and not q):
            self.is_equv = False
            return

        if (p.left and not q.left) \
        or (not p.left and q.left) or (p.right and not q.right) or \
        (not p.right and q.right):

            self.is_equv = False
            return

        if not self.is_equv:
            return 
        
        if p.val != q.val:
            self.is_equv = False
            return
        
        if p.left and q.left:
            self.checkTree(p.left, q.left)

        if p.right and q.right:
            self.checkTree(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.checkTree(p,q)
        return self.is_equv
        
        