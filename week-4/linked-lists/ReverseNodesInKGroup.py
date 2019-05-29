# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2 or not head: return head
        
        # go through and find the starting points to reverse
        i = 1
        starts = []
        ptr = head
        while ptr:
            start = ptr
            while i < k:
                ptr = ptr.next
                i += 1
                
                if not ptr:
                    if not starts:
                        return head
                    break
                    
            if i == k and ptr:
                new_end = ptr
                ptr = ptr.next
                new_end.next = None
                starts.append(start)
                i = 1
                start = ptr
            else:
                break
         
        # reverse each sublist
        for i, node in enumerate(starts):
            starts[i] = self.reverseList(node)
        
        # connect each newly reversed sublist
        for i, node in enumerate(starts[:-1]):
            while node.next:
                node = node.next
            node.next = starts[i+1]
        
        # connect any leftover nodes
        if start != ptr:
            lastlist = starts[-1]
            while lastlist.next:
                lastlist = lastlist.next
            lastlist.next = start
        
        return starts[0]