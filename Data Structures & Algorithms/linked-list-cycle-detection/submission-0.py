# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ 
        input = head of ll

        goal = 
            find out if there is a cycle
                    - if at least 1 node can be reached again via next

        output = t -> if cycle 
                 - f -> if no cycle
                
        
        """
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False