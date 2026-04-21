# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, curNode = None, None
        exp = 1
        step = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            sum_val = l1_val + l2_val + step
            step = 1 if sum_val >= 10 else 0
            sum_val = sum_val % 10

            if not head:
                head = curNode = ListNode(sum_val, None)
            else:
                curNode.next = ListNode(sum_val, None)
                curNode = curNode.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if step > 0:
            curNode.next = ListNode(step, None)
        
        return head