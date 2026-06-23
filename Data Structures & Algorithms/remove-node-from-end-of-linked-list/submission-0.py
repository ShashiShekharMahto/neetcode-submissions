# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def get_len(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        list_len = self.get_len(head)

        del_idx = list_len - n
        if del_idx == 0:
            return head.next

        pos = 0

        curr = head
        prev = None
        while pos <= del_idx:
            if pos == del_idx:
                temp = curr
                curr = curr.next
                temp.next = None
                prev.next = curr
                pos += 1
            else:
                prev= curr
                curr = curr.next
                pos +=1
        return head

        