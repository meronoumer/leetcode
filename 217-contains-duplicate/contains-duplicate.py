class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool


        -   input - array of ints = nums
        - output - 
            t : if any val appears 2x or> in the array
            f : if all vals appear 1 time
        goal 
            - look at 2 things = HASHSET/DICT
                - val
                    - 
                - freq
            init dict
            counter init =0 - here no reset
            traverse through nums 
                
                for each key add it to our dict
                    - add its counter 
                        - if key in dct:
                            count+=1
                                - ret tru?

                        else:
                            counter =0
                            count+=1
                            addk v to dict

            go through dict again 
                - if any vals are greater than 1 
                    - for val in dict.values)-list
                        if val>1:
                            ret twu
                    ret false

        """
        counter = 0
        seen = {}
        for num in nums:
            if num in seen:
                counter+=1
                seen[num]=counter
                return True
            else:
                counter = 0
                counter+=1
                seen[num]=counter
        return False


        
        