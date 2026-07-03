class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            diff = target - num

            # 1. Look backward: Is the number we need already in our dictionary?
            if diff in seen:
                # If yes, return the index of the number we saw earlier,
                # and the index of the current number we are standing on.
                return [seen[diff], index]

            # 2. If not, store the current number and its index in the dictionary
            seen[num] = index