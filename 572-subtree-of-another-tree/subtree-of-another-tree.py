# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False
        if self.isEqual(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    


    def isEqual(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        
        left_sec = self.isEqual(p.left,q.left)
        right_sec = self.isEqual(p.right,q.right)

        return left_sec and right_sec
        