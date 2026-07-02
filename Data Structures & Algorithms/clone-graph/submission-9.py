"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hmap = {node:Node(node.val)}
        q = deque([node])

        while q:
            cur = q.popleft()
            copy = hmap[cur]

            for nei in cur.neighbors:
                if nei not in hmap:
                    hmap[nei] = Node(nei.val)
                    q.append(nei)
                copy.neighbors.append(hmap[nei])
        
        return hmap[node]