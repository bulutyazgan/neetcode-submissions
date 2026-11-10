class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = defaultdict(int)
        for c in s1:
            chars[c] += 1
        
        l = 0
        res = defaultdict(int)
        for r in range(len(s2)):
            res[s2[r]] += 1
            if r - l + 1 > len(s1):
                res[s2[l]] -= 1
                if res[s2[l]] == 0:
                    res.pop(s2[l])
                l += 1
            if res == chars:
                return True
        return False
            
