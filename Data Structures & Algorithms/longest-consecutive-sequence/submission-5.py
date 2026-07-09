class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        input - array  - cont nums

        output - length of longest 
        

        """
        store = set(nums)
        max_streak = 0

        for num in nums:
            if (num-1) not in store:
                streak  =0
                curr = num
                while curr in store:
                    streak+=1
                    curr+=1
                max_streak = max(max_streak,streak)
        return max_streak
