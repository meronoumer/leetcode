class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        if s==s[::-1]:
            return True
        else:
            return False


        # left= 0
        # right = len(s) 
        # if len(s)%2==0:
        #     middle = len(s)//2 - 1
        # else:
        #     middle = len(s)
      

        # if s[:middle +1]== "".join(reversed(s[middle:])):
        #     return True
        # else:
        #     return False

        # for index in range(len(s)):
        #     left+=index
        #     right -=index
        #     print(left)
        #     # print(right)
        #     print (s[left])

        #     if s[left]!=s[right]:
        #         return False
        
        # return True
                




        