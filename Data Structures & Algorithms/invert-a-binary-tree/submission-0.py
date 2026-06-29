# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        input = root of a tree
        output = root of new tree where each 
        root/subtree has had its ch rever

        goal 
            - swapping 
            - while we stll have a root
             - store left child in tmp var
             root.left = root.right
             root.right = temp

            #  update root to frst go left
             - what happens at end 
                    - goes to rght 
                    - we dont want t to get stuk so do we need an 
                    alternate frm of storage for data?



            # update root to then go right
            
        """
        if root is None:
            return None
        
        # 1. Swap your immediate left and right children (Your exact idea!)
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # 2. DELEGATION: Tell the left child to go invert its entire subtree
        self.invertTree(root.left)
        
        # 3. DELEGATION: Tell the right child to go invert its entire subtree
        self.invertTree(root.right)
        
        # Finally, return the root of the flipped tree
        return root

