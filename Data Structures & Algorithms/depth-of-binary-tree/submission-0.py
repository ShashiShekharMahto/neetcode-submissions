# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxCount(self, root):
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1

        l = 0
        r = 0
        if root.left:
            l = self.maxCount(root.left)

        if root.right:
            r = self.maxCount(root.right)
        return 1 + max(l,r) 

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_v = self.maxCount(root)

        return max_v