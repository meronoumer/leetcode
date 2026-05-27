class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        input - list of strings

        pass through the strings
        add in the strings into one init empty string . 
        have a sep of choice ~

        output = one concatenated string?
        """
        encoded_string =""
        for string in strs:
            encoded_string +=string + "~"
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """
        input - one concatenated string? 


        init empty array
        break up string by separator
        append into array
        output =   list of strings


        """
        print(str)
        decoded_strs = s.split("~") 
        decoded_strs.pop()
        return decoded_strs
