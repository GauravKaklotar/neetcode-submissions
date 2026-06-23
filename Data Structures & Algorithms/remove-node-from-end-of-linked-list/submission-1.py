# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ******** 1 pass solution ****************
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Create diff of n steps b/w slow and fast
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next



        # ******** 2 pass solution ****************
        # count = 0
        
        # curr = head
        # while curr:
        #     count += 1
        #     curr = curr.next
        
        # steps = count - n - 1

        # if steps == -1:
        #     return head.next
        # else:
        #     curr = head
        #     while steps:
        #         steps -= 1
        #         curr = curr.next
            
        #     curr.next = curr.next.next
        
        # return head
        
