# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        counts = defaultdict(int)
        curr = head

        while curr:
            counts[curr] += 1
            if counts[curr] == 2:
                return True
            curr = curr.next
            
        return False

        