# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        curr = head
        left, right = 0, len(nodes) - 1
        i = 0
        while left < right:
            if i % 2 == 0:
                curr = nodes[left]
                curr.next = nodes[right]
                left += 1
            else:
                curr = nodes[right]
                curr.next = nodes[left]
                right -= 1
            
            i += 1
        
        if nodes:
            nodes[left].next = None
        
            



            


        
        