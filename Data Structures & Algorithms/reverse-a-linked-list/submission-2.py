# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        past = None
        curr = head
        

        # have everythng pointing to the thing before t 

        while curr:
            future = curr.next
            # curr = future
            curr.next = past
            past = curr
            curr = future
        return past
