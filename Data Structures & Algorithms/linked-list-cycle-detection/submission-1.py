# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        while head.next != None:
            if head.next != None and head.next.val == "visited":
                return True
            elif head.next == None:
                return False
            else:
                head.val = "visited"
                head = head.next
        return False

        