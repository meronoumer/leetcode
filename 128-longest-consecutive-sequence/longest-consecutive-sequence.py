class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int



        input - arr(unsorted) - arr called nums with integers in it 

        output - max length of longest consequ element sequence


        how?
            - 0(n) = iterate thru array 
            - pick up first item in nums
                - convert it into a set - to check if contains in faster lookup 
                - take frst item - see if there is one less than it in set
                    - no:
                        - we have a streak gong !
                            streak=0
                            curr = num
                            inc item-> rename it to avoid infinite loop
                                ->inc that new item
                            if the curreny num is in set
                                - increment again
                        else    
                            - streak = 0




        """
        final_len = 0
        set_nums = set(nums)

        for num in set_nums:
            if (num -1)not in set_nums:
                streak = 0
                curr = num
                while curr in set_nums:
                    streak+=1
                    curr+=1
                final_len = max(final_len,streak)
        return final_len
