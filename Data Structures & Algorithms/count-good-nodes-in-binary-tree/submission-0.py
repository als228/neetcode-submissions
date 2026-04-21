# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        def dfs(root, maxVal):
            nonlocal res
            if root.left:
                if root.left.val >= maxVal:
                    res += 1
                    dfs(root.left, root.left.val)
                else:
                    dfs(root.left, maxVal)
            if root.right:
                if root.right.val >= maxVal:
                    res += 1
                    dfs(root.right, root.right.val)
                else:
                    dfs(root.right, maxVal)
        
        dfs(root, root.val)
        return res