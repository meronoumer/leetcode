# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """

        input = head of ll
        goal = 
         - have two pointers at start , contigously next to each other
         - traverse through once untl we reach teh end and other one finds us the middle
         hav e
         - reassign them to eachother 
                 - have them point to what teh other one is pointing to 
        output = new ead post reversal
        """
        past,curr = None,head

        while curr:
            future = curr.next
            curr.next = past
            past = curr
            curr = future
        return past