# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, low = float("-inf"),high = float("inf")):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
   
        if not (low < root.val < high):
            return False
        
        return self.isValidBST(root.left,low,root.val) and self.isValidBST(root.right,root.val,high) 
        