class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        input - n/int

        output- arr [1....n]
            - div by 3 = "fizz"
            - div by 5 = "buzz"
            - div by 15 - = "Fizzbuzz"

        - set up a 1 indexed range up till that number 
        - check divisibility = iteration
                - 
        - replace = if

        O(n) 
        """
        answer = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer