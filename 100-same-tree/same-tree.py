# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        """
        input = 2 roots of binary trees


        output - t 
                - if ==
            - f
            - if!=
        goal 
            - start with both our roots - check if equal
                    - if both none
                        return true
                    - if one here other none
                        ret f
                    - if not 
                        immediately return false

                    
                    if equal 
                     - go left
                     - check if two nodes equal 
                        - sub chuncks/sub sections 
                            - repeat same instructions
                            - recursively
                                    base case??
                     - go right 
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        
        left_sec = self.isSameTree(p.left,q.left)
        right_sec = self.isSameTree(p.right,q.right)

        return left_sec and right_sec
        