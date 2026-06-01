class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        input 
            = arr = heights of y axs of different bars in a container
        output 
            max amt of water stored = n
                - two lines - tallest lines
                    - tallest line - needs to be subtracted to equal lesser line
        [1,8,6,2,5,4,8,3,7]
        [1,2,3,4,5,6,7,8,8]
        
        using two pointers
            - i could sort the lst 
            - set up a varable n /prod?
                    - init to 1
            set up two pointers at start and end
            multiply pointers and store in prod
                if multiply pointers > prod:
                    inc left by 1
            the number at inex right cant be greater than index left
                - then multiply number at index left by tself and store as prod
            
            return that prod
            """
        # height = sorted(height)
        prod = 1
        l = 0
        r = len(height)-1
        width = 0
        res = 0
        while l<r:
            area = min(height[l], height[r]) * (r - l)
            
            # Update our maximum area if the current area is bigger

            res = max(res, area)
            
            # Move the pointer that has the smaller height
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
        