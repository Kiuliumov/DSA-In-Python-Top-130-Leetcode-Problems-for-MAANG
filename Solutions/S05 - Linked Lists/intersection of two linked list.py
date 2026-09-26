# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        firstListNodes = set()

        curr = headA
        while curr is not None:
            firstListNodes.add(curr)
            curr = curr.next
        
        curr = headB
        while curr is not None:
            if curr in firstListNodes:
                return curr
            curr = curr.next
        return None