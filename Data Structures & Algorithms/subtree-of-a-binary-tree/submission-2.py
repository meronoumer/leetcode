# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        input = root , subroot

        output - T if subroot and its kids/grandkids are in root 
                - F if subroot and its kids/grandkids are not in root 
        
        goal - check if subroot root is in root 
                    - in = save subroot ,check if eq to root
                            then change root 
                                - go left ,go right
                                            - if yes - check if its.left ==.right
                                                repeating step 
                                                recursive

                                        else
                                            - would we keep the same repeating step?
                                            - when do we stop?
                            

        """
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
            



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


        
        