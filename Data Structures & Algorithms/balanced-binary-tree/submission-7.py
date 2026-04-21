# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            lHeight = dfs(node.left)
            rHeight = dfs(node.right)
            if abs(lHeight-rHeight) > 1:
                res = False
            return 1 + max(lHeight, rHeight)
        
        dfs(root)
        return res