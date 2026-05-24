class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        """
        input = array of numbers
        number we are looking for 

        output = 
            - indices of the two addennds

            -

        """
        seen = {}
        for ind,num in enumerate(nums):
            sub = target-num
            if sub in seen:
                return seen[sub],ind
            else:
                seen[num]=ind
        