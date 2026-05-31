class Solution(object):
    def threeSum(self, nums):
        large_arr = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            # FIX 1: Skip duplicate values for 'i' to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum == 0:
                    # FIX 2: Append directly to large_arr
                    large_arr.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    # FIX 3: Skip duplicate values for 'left' and 'right'
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total_sum > 0:
                    right -= 1
                elif total_sum < 0:
                    left += 1

        return large_arr