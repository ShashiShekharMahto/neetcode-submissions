# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        
        while head:
            if head.next == None:
                return False
            if head.next != None:
                head.val = "checked"
            if head.next.val == "checked":
                return True
            head = head.next
        return False


        