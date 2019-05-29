import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if not lists: return lists
        
        heap = []
        for l in lists: # O(n)
            head = l
            while head:
                heap.append(head.val)
                head = head.next
        
        if not heap: return heap
        
        heapq.heapify(heap) # O(n)
        
        new_head = ListNode(heapq.heappop(heap))
        ptr = new_head
        while heap: # O(n)
            ptr.next = ListNode(heapq.heappop(heap))
            ptr = ptr.next
        
        return new_head        