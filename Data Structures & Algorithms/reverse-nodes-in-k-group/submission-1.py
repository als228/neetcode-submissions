# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(node, stop_node):
            if node.next == stop_node:
                return node
            else:
                new_head = reverseList(node.next, stop_node)
                node.next.next = node
                node.next = stop_node
                return new_head
        
        dummy = ListNode(0, head)
        cur = dummy
        
        while cur:
            prev = cur
            cur = cur.next
            next_node = cur

            for _ in range(k):
                if not next_node:
                    return dummy.next
                next_node = next_node.next
            
            prev.next = reverseList(cur, next_node)
        
        return dummy.next