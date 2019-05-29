# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        ptr = head
        
        for i in range(1,3):
            if not ptr:
                return head
            
            if i == 1:
                odd_head = ptr
            else:
                even_head = ptr
            
            ptr = ptr.next
        
        index = 3
        o, e = odd_head, even_head
        while ptr:
            if index % 2 == 0:
                e.next = ptr
                e = e.next
            else:
                o.next = ptr
                o = o.next
                
            ptr = ptr.next
            index += 1
        
        # connect two lists
        o.next, e.next = even_head, None
        
        return odd_head