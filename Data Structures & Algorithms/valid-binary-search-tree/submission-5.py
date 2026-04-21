# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True
            
            validNode = (node.val > min_val and node.val < max_val)
            if validNode: 
                return (not node.left or dfs(node.left, min_val, node.val)) and (not node.right or dfs(node.right, node.val, max_val))
            else: 
                return False
        
        return dfs(root, -1001, 1001)