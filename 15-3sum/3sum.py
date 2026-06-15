class Solution(object):
    def threeSum(self, nums):
        """

        init larg arr
        two pointers
        way of tracking 3rd 
            = iterate thru 
                - for loop
                    for each number in i we could add it to a set and then check the sum of the numbers to the left ad right 
                    if the number at right + th enumber at left is 


        """
        large_arr = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            # FIX 1: Skip duplicate values for 'i' to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left<right:
                total_sum = nums[i]+nums[left]+nums[right]
                if total_sum==0:
                    large_arr.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total_sum>0:
                    right-=1
                elif total_sum<0:
                    left+=1
        return large_arr
