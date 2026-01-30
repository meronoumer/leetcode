class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """
        s,t 
        check if anagram 
                - same letters app same number of times

        imp
            -hash
                -faster look up
                - same letters , freq
            - by looping through the string and adding chars to a prev found hashset

            crosschecking str and hashsets for charachters and similarities
        """
        new_s = "".join(sorted(s))
        new_t = "".join(sorted(t))
        return new_s == new_t


        