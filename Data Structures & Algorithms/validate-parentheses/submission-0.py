class Solution:
    def isValid(self, s: str) -> bool:
        """
        input 
            = string 
                with different charcters 
                if characters close each other then 

        """
        stack = []

        openers = ["(","{","["]
        # str = list(s)
        # Keys are closers, values are openers
        maps = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in openers:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                if stack[-1]==maps[char]:
                    stack.pop()
                elif stack[-1]!=maps[char]:
                    return False
        
        if len(stack)==0:
            return True
        else:
            return False

