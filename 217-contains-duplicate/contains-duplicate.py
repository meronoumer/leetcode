class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """

        go through an array 



        return true
         - if theres any value that appears more than once in the array
        /false
            - if all elems appear once/singularly in the array

        
        -go through the array  = for loop
        initialize a dictionary seen= {}
        for each element set add it into the dict as key seen[key]=1
                         - add in its 1(no of times it appears) as a value

                                alr. seen element
                                    - increment that value by 1 of element b y1
                                if el in seen:
                                    seen[key]+=1
                                else:
                                    seen[key]=1


        
        2nd half
            - check if there are any elements with value >1 in the dictionary
            for elem in seen:
                if seen[elem]>1
                    ret True
                else:
                        ret False

        """
        seen = {}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        
        print(seen)
        for key,value in seen.items():
            print(value)
            if value>1:
                print(value)
                return True
            else:
                continue
        
        return False

        