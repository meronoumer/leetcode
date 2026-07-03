class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        input = s,t 



        output 
            T 
                - if t is an anagram of s 
                    - same letters same no of letters
            F
                - f not 
        
        goal 
            - B.F 
                = sort both 
                    - o(nlog(n))
                = compare them ==
            - use 2 dictionaries
                - letter 
                - freq
            then if we have same dicts
                - t else f
        """
        s_dict = {}
        t_dict = {}



        for s_char in s:
            if s_char in s_dict:
                s_dict[s_char]+=1
            else:
 
                s_dict[s_char]=1
            
        for t_char in t:
            if t_char in t_dict:
                t_dict[t_char]+=1
            else:

                t_dict[t_char]=1

        return s_dict==t_dict
            

        