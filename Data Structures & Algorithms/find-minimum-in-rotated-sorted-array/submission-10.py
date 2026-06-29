class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        find where the sections chunk off 
        like wats the first secton vs the second section

        and then just return the first number 
        in the second section


        - have a pointer at the start 
            - keep t there
        -have a second pointer that keeps incrementin 
        through the array


        then the second we find a pointer that is less than what is at the start
        return it



        """
        left,right = 0,len(nums)-1
        if nums[left]<nums[right]:
            return nums[left]

        while left<right:
            mid = (left + right)//2

            if nums[mid]>nums[right]:
                left = mid +1
            else:
                right = mid
        return nums[left]


        