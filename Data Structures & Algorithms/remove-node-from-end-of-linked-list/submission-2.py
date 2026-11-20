# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        # count length
        while curr:
            length += 1
            if curr.next and not curr.next.next:
                penultimate = curr
            curr = curr.next
            

        # remove first or last element
        if n == length:
            return head.next
        elif n == 1:
            penultimate.next = None
            return head

        # remove intermediate
        target = length - n
        curr = head
        i = 0
        while curr:
            if i == target - 1:
                prev = curr
            elif i == target + 1:
                prev.next = curr
            curr = curr.next
            i += 1

        return head



