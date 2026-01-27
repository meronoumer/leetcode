class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        input =  arr has ints

            return t = if val repeats
            return f = if every val is once

        iterating 

            for loop thru arr
                - vals, indices = enumarate()
            - hashmap for val,indice pairs - for checking later 
            O(n)

        """
        seen = {}
        for index,num in enumerate(nums):
            seen[num] = index
        
        for index,num in enumerate(nums):
            if num in seen and seen[num]!=index:
                return True
        
        return False

        