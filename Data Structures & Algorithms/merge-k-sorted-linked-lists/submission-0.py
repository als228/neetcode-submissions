# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # initialize minheap
        minheap = []
        for i, ll in enumerate(lists):
            if ll:
                heapq.heappush(minheap, (ll.val, i, ll))
        # create a sorted ll
        head = prev = None
        while minheap:
            val, index, cur = heapq.heappop(minheap)
            if not head:
                head = cur
                prev = cur
            else:
                prev.next = cur
            
            if cur.next:
                heapq.heappush(minheap, (cur.next.val, index, cur.next))
            prev = cur
        
        return head