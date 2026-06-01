import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(char for char in s if char not in string.punctuation)
        strip_s = clean_s.replace(" ", "").lower()
        reverse_s = strip_s[::-1]
        return strip_s == reverse_s
        