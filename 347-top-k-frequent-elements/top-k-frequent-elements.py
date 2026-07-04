class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]



        input 
            - nums - array of numbers
            - k = number of most frequent elements that appear

        output 
            - arr of k most freq app nums
        goal 
             - init a dict 
                - looking at two things 
                    - num
                    - no of times they appear
                js update dct on freq and 

                how to access k 
                    - how to access the most freqently app ones
                    can i arrange them n the order of 
                     ---sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    ret that values by slicing to k+1
        """

        seen = {}


        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        sorted_keys = sorted(seen.keys(), key=lambda x: seen[x], reverse=True)

        return sorted_keys[:k]

        