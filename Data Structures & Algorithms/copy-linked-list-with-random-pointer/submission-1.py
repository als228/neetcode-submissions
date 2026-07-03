"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hmap = {head:Node(head.val)}
        q = deque([head])

        while q:
            cur = q.popleft()
            copy = hmap[cur]
            if cur.next:
                if cur.next not in hmap:
                    hmap[cur.next] = Node(cur.next.val)
                    q.append(cur.next)
                copy.next = hmap[cur.next]
            if cur.random:
                if cur.random not in hmap:
                    hmap[cur.random] = Node(cur.random.val)
                    q.append(cur.random)
                copy.random = hmap[cur.random]
        
        return hmap[head]