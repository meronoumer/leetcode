# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        """
        input 
            - BT - root
        output 
            - array of sub arrays
                 = showing all nodes.vals on one level
        goal 
            - do a bfs
                - @ level  - if u see some add sumn
            init records = []
            init a queue
            while queue
                small_rec = []
             - get length of that queue
                    - ill set it as the ran ge for the second per level iter
                    how many  x to go each level
                    for loop by range

                        see node = pop off end of queue
                            - add it to small_rec
                        
                        if node has left
                            - add it to queue
                        if has right
                            - add it to queue
                    records.append(small_arr)
            out of while - ret records
        """
        if not root:
            return []
        
        records = []
        queue = deque([root])
        while queue:
            small_rec = []
            len_que = len(queue)
            for _ in range(len_que):
                node = queue.popleft()
                small_rec.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            records.append(small_rec)
        return records
        