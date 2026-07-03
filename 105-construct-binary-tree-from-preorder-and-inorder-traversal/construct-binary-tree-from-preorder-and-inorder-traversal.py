# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]

        input - two arrs of ints 
            preorder
                - root,left,right - trav

            inorder
                - left,root,right -terav
        output - 
            - root of bst that has these node.vals in this resp. travellers 
            - root how?
                - preorder 1st el [0]  = root
                rest of tree?
                    - 





        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root

        