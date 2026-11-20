# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        # turn head into tail
        curr = head
        next_el = curr.next 
        curr.next = None

        # reverse list
        while next_el.next is not None:
            coming = next_el.next
            next_el.next = curr
            curr = next_el
            next_el = coming

        # turn tail into head
        next_el.next = curr
        head = next_el
        
        return head




        


        


        