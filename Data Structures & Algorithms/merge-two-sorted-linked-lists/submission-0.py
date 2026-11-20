# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        head = current
        prev = None

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        while list1 is not None and list2 is not None:
            # compare values
            if list1.val <= list2.val:
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next

            # link previous to current
            if prev is not None:
                prev.next = current

            # update previous
            prev = current

            # create new element
            current = ListNode()

        if prev is None:
            return head

        if list1 is None:
            prev.next = list2
        elif list2 is None:
            prev.next = list1

        return head

        
