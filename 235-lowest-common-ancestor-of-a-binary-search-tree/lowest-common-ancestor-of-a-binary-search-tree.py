# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """

        input : - root of BST 
                - P ,Q WHICH ARare two nodes n bst 
        output 
            - LCA of p and q
                - An ancestor of a node is any node that sits directly above it on the path back to the very top (the root).
                - A common ancestor of two nodes is a node that sits above both of them.
        goal 
            - go through our BST 
                - rec
                - iter 
            BST  = key to solving ths
                - left of root always less
                - right "" >
                    - connect p,q and the root of BST
            - so check pval and q val
                case 1
                    - if both less
                        go right
                        root = root.right
                    - if both >
                        go left
                    - if one> and other< or if p/q are root
                        we've found where they diverge/split/pivot 
                        - no more com anc below = pivot = LCA = ROOT
                        ret root      
        """
        #c1
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root