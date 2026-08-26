class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(reversed("".join(c.lower() for c in s if c.isalnum())))
        string2 = "".join(c.lower() for c in s if c.isalnum())

        return string == string2
        