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

        # simplest way 
        # new_s = "".join(sorted(s))
        # new_t = "".join(sorted(t))
        # return new_s == new_t

        # by hashing 



        s_seen = {}
        s_counter = 0
        t_seen = {}
        t_counter = 0
        for s_char in s:
            if s_char not in s_seen:
                s_counter = 1
                s_seen[s_char]= s_counter
            else:
                s_counter = s_seen[s_char]
                s_counter +=1
                s_seen[s_char]= s_counter
        for t_char in t:
            if t_char not in t_seen:
                t_counter = 1
                t_seen[t_char]= t_counter
            else:
                t_counter = t_seen[t_char]
                t_counter +=1
                t_seen[t_char]= t_counter

        print(dict(sorted(s_seen.items())))
        print(dict(sorted(t_seen.items())))

        print(s_seen == t_seen)

        return s_seen == t_seen





        