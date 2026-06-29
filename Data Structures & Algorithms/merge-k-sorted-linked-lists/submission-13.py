# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        input - 1 large lst
                    - cont several lls where internallly are sorted asc(nodes inc)
        

        output
            - 1 final linked list
            -   sorted linked list in asc ord of nod vals
                 - ret head of the new lnked list
        
        goal = 
            set up a new dummy node
            traverse through all lls at the same time
            for each head - compare them 
                - 
            if less attach it to dummy node
            add one that is greater to that one and thenn after

            do it for two and then save that as merged and if our lists is not empty then keep working on lists
            

            

        edge cases
            - if empty 
                return None
            - not all will be the same sze

        """
        if len(lists)==0:
            return None
        
        
        merged_list = lists[0]
        for i in range(1,len(lists)):
            current_list = lists[i]
            dummy = ListNode("Empty")
            tail =dummy

            head_1 = merged_list
            head_2 = current_list

            while head_1 and head_2:
                if head_1.val<head_2.val:
                    tail.next= head_1
                    head_1 = head_1.next
                else:
                    tail.next = head_2
                    head_2 = head_2.next
                tail = tail.next
            # If head_1 still has nodes left, append them and move tail forward
            while head_1:
                tail.next = head_1
                head_1 = head_1.next
                tail = tail.next

            # If head_2 still has nodes left, append them and move tail forward
            while head_2:
                tail.next = head_2
                head_2 = head_2.next
                tail = tail.next
                        
            merged_list = dummy.next
            


        return merged_list

            

            

        