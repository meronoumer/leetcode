class Solution:
    # We add low and high directly into the main function with default values!
    def isValidBST(
        self,
        root: Optional[TreeNode],
        low=float("-inf"),
        high=float("inf"),
    ) -> bool:
        # 1. Base case: an empty branch is always valid
        if not root:
            return True

        # 2. Check if the current node breaks the grandparent rules passed down to it
        if not (low < root.val < high):
            return False

        # 3. Recursion handles the subtrees by updating the boundaries directly!
        # When going left, update the high ceiling to root.val
        # When going right, update the low floor to root.val
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(
            root.right, root.val, high
        )