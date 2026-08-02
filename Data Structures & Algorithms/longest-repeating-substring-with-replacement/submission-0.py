class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1 or len(s) == k:
            return len(s)
        ans = 0

        l, r = 0, 0
        maxf = 0
        count = {}

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]]) 

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1

        return ans
