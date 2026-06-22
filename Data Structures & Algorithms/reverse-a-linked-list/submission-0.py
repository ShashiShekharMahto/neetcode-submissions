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
        next_l = head.next
        curr.next = None
        head = next_l

        while head.next != None:
            temp = head
            next_l = head.next
            temp.next = curr
            curr = temp
            head = next_l
        
        head.next = curr
        return head
        
        

            

        