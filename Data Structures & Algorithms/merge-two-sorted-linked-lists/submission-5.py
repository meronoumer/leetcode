# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        input = 2 heads of sorted lls

        goal =
        start a new ll
             - starting node

             ending node = be at start init 
                            = traverse to end  
         iterate through both our lls = = while = l1 and l2 are still not null
         compare values at each node
         if one val greater thanother , comes after

             - .next of lesser node to that of bgger node
        if less
            rev
            connect 2 then connect 5 

        tail = tail.next 
            // so we're moving tail
        
        if l1:
            // bc alr sorted
            add onto tail
                - tail.next = l1
        elif l2:
            add onto tail 
                tail.next = l1
        return starter.next

        ///but how would started get updatedf??

        edge cases:
            - if two empty lists
                cant sort them so t will retunr none
            - if one empty and other isnt        

        output = a merged one sorted lst 
        
        """
        starter = ListNode()
        ender = starter

        while list1 and list2:
            if list1.val<list2.val:
                ender.next = list1
                list1 = list1.next #cause i see no reason to abandon list2
            else:
                ender.next = list2
                list2=list2.next # or is this just us solely incrementing through and maing sure we are traversng teh lst 
            ender = ender.next
        if list1:
            ender.next = list1
        elif list2:
            ender.next = list2
        

        return starter.next





