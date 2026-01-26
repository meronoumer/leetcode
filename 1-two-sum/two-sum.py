class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        input = arr w x nums
        output = indices of numbers that add to give us the target

        iterate through arr
        have two pointers
        whenever two pointers add up to a target then end loop and return the indices of those two vals

        for time
            - no nested for loop
                - initialize the index of both ptrs and update as we go along 


        """
        set_indices = set()
        dict = {}
        for num_ind in range(len(nums)):
            if target-nums[num_ind] in dict:
                return [dict[target-nums[num_ind]],num_ind]
            else:
                dict[nums[num_ind]]= num_ind

