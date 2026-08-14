# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
             return None
        cur = head
        fwd = cur.next
        while fwd != None:
            temp = fwd.next
            fwd.next = cur
            cur = fwd
            fwd = temp
        
        head.next = None
        head = cur
        return head
        