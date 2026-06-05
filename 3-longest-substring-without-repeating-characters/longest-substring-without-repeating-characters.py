class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int


        - input 
            str = s
        
        # largest = ""
        substr=""
        output 
            str of chars that arent repeating /n the order they appear
        init empty str = 
        we start by tracking one letter
        and then we check the one next to it
                = two pointer techniq
            if next != current
                add next + current = string 
                if len(largest)<len(substr):
                    largest=substr
            else:
                largest = save it

        return largest after done wiz whle loop


        """
        first = 0
        seen = set()
        max_len = 0
        for second in range(len(s)):
            while s[second] in seen:
                seen.remove(s[first])
                first+=1
            
            seen.add(s[second])

            max_len = max(max_len,second-first+1)
        return max_len
                
