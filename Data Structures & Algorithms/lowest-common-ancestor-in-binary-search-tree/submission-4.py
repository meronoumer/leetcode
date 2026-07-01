# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        input - 
            BST 
                - ALL TOO RIGHT OF NODE>NODE
                - v.v
            two nodes - p,q 

        output - LCA of p & q
               - parent/grandparent that p and q have in common 
                but if theres a parent in com/no grandparent 
             - it can be its own descendant 
        goal 
             - BST 
                - bc of less/gre l/r structure 
                - helps us find p and q with root 
                    - update by root
                - case
                    -  if we see they're both > st root
                        - move right 
                            - root = roogh.rght
                    -    vv 

                    - if one less and another  greater 
                        - we've found the pivot
                            - return root = lca

        """
        if not root:
            return None
        
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
        