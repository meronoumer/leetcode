class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]




        input - array of numbers - a number - targ. that two nums could sum to 

        output 
            - array of indidces of where these addends are located
        goal 
            - use dict 
                - tracking for two things
                - num itself
                - indices - where it is
            - traverse nums
                - add to dict + location
            - now use target and iteratively calculate the diff between all keys and target 
                if diff in dic 
                    - yes - ret ind of diff and 
                
                

        """
        seen = {}
        for index,num in enumerate(nums):
            diff = target-num
            if diff in seen:
                return [seen[diff],index]
            seen[num]=index





        