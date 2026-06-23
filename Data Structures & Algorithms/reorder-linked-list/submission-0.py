# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def get_len(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
    
    def reverse_list(self, head:Optional[ListNode]):
        
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


    


    def reorderList(self, head: Optional[ListNode]) -> None:


        list_len = self.get_len(head)

        mid_val = list_len//2

        mid = mid_val + 1  if list_len % 2 != 0 else mid_val

        curr = head
        prev = None

        while mid != 0:
            prev = curr
            curr = curr.next

            mid -=1
        
        prev.next = None

        first_half = head
        second_half = self.reverse_list(curr)

        while first_half and second_half:
            temp = second_half.next
            temp2 = first_half.next

            first_half.next = second_half
            second_half.next = temp2

            first_half = temp2
            second_half = temp
            





        
        


        