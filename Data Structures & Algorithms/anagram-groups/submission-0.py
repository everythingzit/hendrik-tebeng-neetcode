class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        sorted_map = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in sorted_map:
                sorted_map[sorted_string].append(string)
            else:
                sorted_map[sorted_string] = [string]
        
        for word_list in sorted_map.values():
            output.append(word_list)

        return output