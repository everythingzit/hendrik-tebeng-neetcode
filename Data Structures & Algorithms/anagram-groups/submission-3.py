class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagrams = defaultdict(list)

        for word in strs:
            alpha = [0] * 26
            for c in word:
                order = ord(c) - ord("a")
                alpha[order] += 1
            anagrams[tuple(alpha)].append(word)
        
        for value in anagrams.values():
            output.append(value)
        
        return output