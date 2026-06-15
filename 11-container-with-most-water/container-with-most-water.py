class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        """
        max_area = 0
        left = 0
        right = len(height)-1
        res = 0
        
        
        while left<right:
            width = right-left
            max_area = min(height[right],height[left])*width
            res = max(res,max_area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return res


