# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        steps = count - n - 1

        if steps == -1:
            return head.next
        else:
            curr = head
            while steps:
                steps -= 1
                curr = curr.next
            
            curr.next = curr.next.next
        
        return head
        
