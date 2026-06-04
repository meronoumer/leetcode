class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int



        - input = arr of prices 
        - pck one day to buy one stock 
        - pick different day to sell that stock 

        find max profit 
            - we're tracking for two things 
            so we want a two sized moving window
                that's going to subtract those two numbers = store that 
                init max_prof = 6



                    - no sort - pos matters
        return it 
            or if no max 
                - return 0c
                    case
                        - if the prices earlier are higher than th eprices later 
                                = loss selling for lower than it was bought

        day we buy
            - 7
            if diff is negative 
                no sell 
                check next

                brute force
                    - grab one 
                        run comparisions for all across the board 
        left = 
        rght = end of arr
        min_price = prices[0]
        max_profit = 0
        """
        # min_price = prices[0]
        max_profit = 0

        buy_day = 0
        sell_day = 1

        while sell_day<len(prices):
            if prices[buy_day]<prices[sell_day]:
                profit = prices[sell_day]-prices[buy_day]
                max_profit = max(profit,max_profit)
            else:
                buy_day = sell_day


            sell_day+=1
        
        return max_profit


        