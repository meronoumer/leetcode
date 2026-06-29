# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        input = roots of two trees

        output - true 
                    - if trees are equivalent
            - false
                - if trees are not equivalent
            
        goal = 

            start from both roots
            check if ==
             - not 
                ret false
            else;->
              - go left
               - recurson = call ist(root.left)

              - go right
                ecurson = call ist(root.right)
            

                 finally return true
            base case
                 - if they're both none
                    - return true
                     - if condition 

        """
        if not p and not q:
            return True

        if not p or not q:
            return False
        if p.val!=q.val:
            return False

        left_true  = self.isSameTree(p.left,q.left)
        right_true = self.isSameTree(p.right,q.right)
        return left_true and right_true








        