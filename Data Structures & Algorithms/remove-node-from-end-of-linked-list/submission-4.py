# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        input = head of a linked list 
        goal = add everything into an array = index access
            - 

        output = head of new linked list with nth node removed
        """
        dummy = ListNode(0)
        dummy.next = head
        slow,fast = dummy,dummy

        for num in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


        