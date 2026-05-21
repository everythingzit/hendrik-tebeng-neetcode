class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        setS, setT = {}, {}

        for i, c in enumerate(s):
            setS[s[i]] = setS[s[i]] + 1 if s[i] in setS else 0
            setT[t[i]] = setT[t[i]] + 1 if t[i] in setT else 0

        return setT == setS