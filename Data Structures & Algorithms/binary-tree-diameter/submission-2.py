# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path = 0
    def maxDepth(self, root, max_v):
        if not root:
            return 0, 0
        
        
        l = 0
        r = 0
        if root.left:
            l = self.maxDepth(root.left, max_v)
            
        if root.right:
            r = self.maxDepth(root.right, max_v)

        path_len = l + r
        self.max_path = max(l+r, self.max_path)

        max_v = 1 + max(l, r)
        return max_v
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxDepth(root, 0) 
        return self.max_path
        