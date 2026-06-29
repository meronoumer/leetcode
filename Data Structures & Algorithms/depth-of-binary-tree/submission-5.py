# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        input = root of a binary tree

        output = depth 
                    - max no of nodes down the many paths
        goal
            -   i'd have a length and max length tracker that i'll update if largee
             - init both to 0

             set a base case
                - if root is none?
                    return 0?

                length +=1
                max_length = max(max_length, length+=1)
                
                have counting logic
                have max determining logic

                call function for left side

                call function for rigt side
        edge cases:
            - unbalanced trees?
                - handle well

        return max_length


        """
            # this is causing it to reset to 0 each time , how to avoid....should i do like 1+ self.maxDepth(root.left)

        if not root:
            return 0


        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1+ max(left_depth,right_depth)
        