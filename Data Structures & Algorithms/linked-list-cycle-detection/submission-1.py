# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        freqMap = {}
        cur = head

        while cur not in freqMap:
            if cur == None:
                return False
            freqMap[cur] = 1
            cur = cur.next
        return True
        
            
       
        