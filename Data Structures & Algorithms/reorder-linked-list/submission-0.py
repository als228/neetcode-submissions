# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curNode = head
        length = 0

        def dfs(node):
            nonlocal curNode, length
            if not node:
                return
            
            index = length
            length += 1

            dfs(node.next)
            if length // 2 == index:
                node.next = None
                return
            elif length // 2 > index:
                return
            
            node.next = curNode.next
            curNode.next = node
            curNode = node.next
        
        dfs(head)