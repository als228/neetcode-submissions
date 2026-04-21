# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None and list2 != None:
            return list2
        elif list1 != None and list2 == None:
            return list1
        
        if list1.val > list2.val:
            newHead, list2 = list2, list2.next
        else:
            newHead, list1 = list1, list1.next
        
        newHead.next = self.mergeTwoLists(list1, list2)

        return newHead