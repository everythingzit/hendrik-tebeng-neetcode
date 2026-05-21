class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = {}
        t_chars = {}
        for i, c in enumerate(s):
            s_chars[s[i]] = s_chars[s[i]] + 1 if s[i] in s_chars else 1
            t_chars[t[i]] = t_chars[t[i]] + 1 if t[i] in t_chars else 1

        return s_chars == t_chars
