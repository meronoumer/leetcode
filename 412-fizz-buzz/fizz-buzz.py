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
        answer=[]
        
        for num in range(1,n+1):
            key = num
            if num%3==0:
                key="Fizz"
                if num%5==0:
                    key+="Buzz"
            elif num%5==0:
                print(num)
                key="Buzz"
            else:
                key = str(key)

            answer.append(key)
        return answer
