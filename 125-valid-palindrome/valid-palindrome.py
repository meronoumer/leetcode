class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool


         - input 

         - output

         bool
            -true
                reads the same forward and backward
            -false
                -o reads the same forward and backward
        

        simplest 
            - keep the first string 
            - reverse the secod string 
                - splicig 
            return f they're equivalent 

            - o(n)
                - iter remove any no al num   
                - lower

        
        two pointer
            have an index ptr at start and end of my string 

                check f equal - iteratively
                    not 
                        return false
                
                
                return true

                const
                    - start< end

                 
                 s .lower()
                 = while loop
                  - if char at left is not alphanumeric 
                    tehn increment by one
                    or at right is not alpha numeric :
                    decremeent by one
        """
        s = s.lower()

        start = 0
        end = len(s)-1
        while start<end:
            if not s[start].isalnum():
                start+=1
                continue
            elif not s[end].isalnum():
                end-=1
                continue
            if s[start]!=s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
        