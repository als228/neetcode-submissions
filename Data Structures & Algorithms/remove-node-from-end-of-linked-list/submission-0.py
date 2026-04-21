# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leftNode = self.findNode(head, None)
        for i in range(n):
            targetNode = leftNode
            try:
                leftNode = self.findNode(head, leftNode)
            except: # if targetNode is head 
                head = head.next
                return head
        
        leftNode.next = leftNode.next.next
        return head
    
    def findNode(self, head, target):
        if head.next == target:
            return head
        
        return self.findNode(head.next, target)