import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        chars = [c.lower() for c in s if c not in string.punctuation]
        clean_s = "".join(chars)
        return clean_s == clean_s[::-1]