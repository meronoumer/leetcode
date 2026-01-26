class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        using built in functions
            convert the number into its binary form
        then count the number of none zeros(1s)
        """

        n_bit = bin(n)
        print(n_bit)

        counter = 0
        for num in n_bit[2:]:
            # print(num)
            if int(num)!=0:
                print(num)
                counter+=1
        return counter
        