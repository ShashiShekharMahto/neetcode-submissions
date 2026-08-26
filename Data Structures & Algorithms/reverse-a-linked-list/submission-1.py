# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or head.next == None:
            return head
        
        curr = head
        curr_next = head.next
        curr.next = None
        head = curr_next
        
        while head.next != None:
            curr_next = head.next
            head.next = curr
            curr = head
            head = curr_next
        
        head.next = curr
        return head
        
        

            

        