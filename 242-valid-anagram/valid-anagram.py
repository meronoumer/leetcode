class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # s = "".join(sorted(s))
        # t = "".join(sorted(t))

        """
        input = strings 1 and 2 
        output = boolean


        t
            - if anagram = if they have the same letters and same number of letters
                            + order doesnt matter
        check by 
            - storing = > k,v = >hashmap
            - compare the two hashmaps to eachother 
            
        """
        if len(s)!=len(t):
            return False
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char]=1
            else:
                s_dict[char]+=1
        
        t_dict = {}
        for char in t:
            if char not in t_dict:
                t_dict[char]=1
            else:
                t_dict[char]+=1


        return s_dict ==t_dict

