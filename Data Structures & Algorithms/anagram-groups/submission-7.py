class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        map = {}

        for string in strs:
            s = "".join(sorted(string))
            if s in map:
                output[map.get(s)].append(string)
            else:
                output.append([string])
                map[s] = len(output) - 1
        return output