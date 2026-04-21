# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        res = []

        if root: 
            queue.append(root)
            res.append([root.val])
            nodesPerLevel = 1
        
        while queue:
            level = []
            prevLevel = 0
            for i in range(nodesPerLevel):
                node = queue.pop(0)
                if node.left:
                    prevLevel += 1
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    prevLevel += 1
                    queue.append(node.right)
                    level.append(node.right.val)
            nodesPerLevel = prevLevel
            if level: res.append(level)
        
        return res