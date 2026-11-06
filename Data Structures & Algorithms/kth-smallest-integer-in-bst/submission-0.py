# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        c = 0
        val = None

        def dfs(node):
            nonlocal c, val
            
            if not node:
                return
            
            dfs(node.left)
            c += 1
            if c == k:
                val = node.val
                return 
            
            dfs(node.right)
            
        
        dfs(root)
        return val
        