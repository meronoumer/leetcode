class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        implement same logic as the earlier anagrams question but then add in an array that is set within an iterative loop so it is added to the big array and return big array
        """

        # big_arr = []
        # small_arr = []

        # first = 0
        # second = 0
        # for str in strs :
        #     if "".join(sorted(str)) != small_arr[0]:


        #     elif str not in small_arr:
        #         small_arr.append(str)
        #     elif "".join(sorted(str)) not in small arr:

        #         small_arr.append(str)
                

        #     big_arr.append(small_arr)
        # print(big_arr)


           

        # # s_seen = {}
        # # s_counter = 0
        # # t_seen = {}
        # # t_counter = 0
        # # for s_char in s:
        # #     if s_char not in s_seen:
        # #         s_counter = 1
        # #         s_seen[s_char]= s_counter
        # #     else:
        # #         s_counter = s_seen[s_char]
        # #         s_counter +=1
        # #         s_seen[s_char]= s_counter
        # # for t_char in t:
        # #     if t_char not in t_seen:
        # #         t_counter = 1
        # #         t_seen[t_char]= t_counter
        # #     else:
        # #         t_counter = t_seen[t_char]
        # #         t_counter +=1
        # #         t_seen[t_char]= t_counter

        # # print(dict(sorted(s_seen.items())))
        # # print(dict(sorted(t_seen.items())))

        # # print(s_seen == t_seen)

        # # return s_seen == t_seen
        anagrams ={}
        if len(strs) ==0:
            return []
        elif len(strs) ==1:
            return [strs]
        

        for word in strs:
            # if word == "":
            #     return strs
            count = [0]*26
            for char in word:
                count[ord(char)- ord('a')]+=1
            if tuple(count) not in anagrams:
                anagrams[tuple(count)]= []
            
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())     






        