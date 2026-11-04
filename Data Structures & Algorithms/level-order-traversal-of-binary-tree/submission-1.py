# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        output = []
        queue = []
        temp = []
        if not root:
            return output
        
        output.append([root.val])
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        queue.append("l")

        if len(queue) == 1:
            return output
        
        while True:           

            if not queue:
                return output

            elem = queue.pop(0)
            if elem != 'l':
                temp.append(elem.val)
                
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            else:
                queue.append("l")

                output.append(temp)
                temp = []
                if not queue or len(queue) == 1:
                    return output
            