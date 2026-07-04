class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]




        input 
            - big array w many strs
        output 
            - big arr
                const small arrs
                    - all of which are anagrams of eachother
        goal 
            - init. a dict 
            - terate through large arr
            for each char
    `           - sort each str we're on
                -add to dct - dict[sorted]=val
                - see if sorted str is alr in dict
                    - if no add 
                    - if yess
                            - append to the value
                                dict[sorted].appe(str)
                - 
            ret values of the dict

        """
        seen ={}

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in seen:
                seen[sorted_str]=[str]
            else:
                seen[sorted_str].append(str)

        return list(seen.values())

        