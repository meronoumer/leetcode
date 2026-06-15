class Solution(object):
    def isPalindrome(self, s):
        """
        - lowercasing 
        - removing all non-alpha nums

        frst letter = last letter
        next = next 
        etc....


        2 ptr

        have something ptg at start of string
        have one at the end

        once not equal 
            - terminate 
                return false
        if equal
            - keep going 
                - iterating 
                    start <end  = indices
        

        """
        s = s.lower()
        left = 0
        right = len(s)-1
        print
        while left<right:
            
            
            if not s[left].isalnum():
                left+=1
                continue
            elif not s[right].isalnum():
                right-=1
                continue

            if s[left]!=s[right]:
                return False

            else:
                left+=1
                right-=1
        return True
