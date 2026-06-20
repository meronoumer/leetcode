class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        - input = arr = prices 
                        - at index i , = val = how much neetcoin goes for each day 
                                        (the price at that day)

        -output = max possible profit
                    - d/c
                     - smallest earlier date/largest later date
                     where largest should not be less than smallest
        goal :  look at the prices of neetcoin at each day 
                - track the difference between the price at this day and a day afterr 
                have the profit var init 
                take the difference

                have the maximum between the var and the ifferemce and uodate ti that 


                how we can check every single combo 
                    - b.f = nested for lop and check for each a , then all bs etc
                

                we can have two ptrs
                    - at start 
                    and then 1 next to it 
                    if the second one i slarger than the first one then 
                        skip ths combo
                            - means move left 
                            - move right 
                    else:
                        take their dfference
                        updat our max_var with the max between max var and difference 
                        only increment right
                        continue the loop = first pont not past the end
        """
        left = 0
        right = 1
        max_diff = 0

        while right<len(prices):
            if prices[left]>prices[right]:
                left=right
                right+=1
            else:
                diff = prices[right]-prices[left]
                max_diff = max(max_diff,diff)
                right+=1
        return max_diff
          

      
