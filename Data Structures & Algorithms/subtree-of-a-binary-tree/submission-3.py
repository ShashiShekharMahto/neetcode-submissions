# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.is_equv = False
        self.any_subroot_val_match = False
    
    def checkTree(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.checkTree(p.left, q.left) and
                self.checkTree(p.right, q.right))  

    def iterateTree(self, root, subRoot):
        if not root and not subRoot:
            self.is_equv = True
            self.any_subroot_val_match = True
            return
        
        if root.val == subRoot.val:
            self.any_subroot_val_match = True

            self.is_equv = self.checkTree(root, subRoot)
        
        if not self.is_equv:
            if root.left:
                self.iterateTree(root.left, subRoot)
            if root.right:
                self.iterateTree(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.iterateTree(root, subRoot)

        if self.any_subroot_val_match:
            return self.is_equv
        return False
        