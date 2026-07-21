class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for c in s:
            if c in d1.keys():
                d1[c] += 1
                continue
            d1[c] = 1

        for c in t:
            if c in d2.keys():
                d2[c] += 1
                continue
            d2[c] = 1
        
        return d1 == d2