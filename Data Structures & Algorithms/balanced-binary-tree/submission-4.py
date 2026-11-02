# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.is_balanced = True

    def checkBalance(self, root):

        if not self.is_balanced:
            return 
        if not root:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        l, r = 0, 0
        if root.left:
            l = self.checkBalance(root.left)
        if root.right:
            r = self.checkBalance(root.right)
        
        if not self.is_balanced:
            return 

        if abs(r - l) > 1:
            self.is_balanced = False
            return
            
        return 1 + max(l, r)
        
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.checkBalance(root)
        return self.is_balanced
        