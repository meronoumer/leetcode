class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:

            if num in dict:
                
                dict[num]+=1 
                   
            else:

                dict[num]=1
            
        
        



        # val = -float("inf")
        # val_arr = []
        # for key,freq in dict.items():
        #     # if freq>val:
        #     val_arr.append([key,freq])
        # val_arr.sort(reverse = True)

                # val_arr[0]=key
            # if dict[val_new] < val:
            #     val_arr.append(key)

        # build array in descending order
        #  then finally return truncated version
        val_arr = []
        for key, count in dict.items():
            val_arr.append([count, key])  # ← keep frequency!

        val_arr.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(val_arr[i][1])

        return res



        