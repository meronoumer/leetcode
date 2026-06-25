# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """ 
        """
        input = head of ll

        goal = 
            find out if there is a cycle
                    - if at least 1 node can be reached again via next
                     - traversing the linked list 
                     as we traverse adding it to a set bc we are checking if it is contained in prior
                        - init a set 
                        - traverse list 
                        - as traverse 
                            check if node in set 
                                - if it is 
                                    break = return true
                            
                                else:   
                                    add the node to the set 
                            end of loop    
                                - return false

        output = t -> if cycle 
                 - f -> if no cycle
                
        time comp = O(n)


        """
        # seen = set()
        # curr = head
        # while curr:
        #     if curr in seen:
        #         return True
        #     else:
        #         seen.add(curr)
        #         curr = curr.next
        
        # return False
        """
        two pointer
            slow = 
            fast

        """
        slow ,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
  
                
        return False
