class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        
        
        for k, v in d1.items():
            if k not in d2.keys():
                return False
            if d2[k] != v:
                return False
            d2.pop(k)
        
        if len(d2.keys()) != 0:
            return False

        return True
        