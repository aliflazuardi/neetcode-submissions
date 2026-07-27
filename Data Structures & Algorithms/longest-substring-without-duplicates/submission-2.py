class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLen = 0
        seen = set()

        i, j = 0, 0
        while j < len(s):
            if s[j] in seen:
                found = False
                while not found:
                    if s[i] ==  s[j]:
                        found = True
                    else:
                        seen.remove(s[i])
                    i += 1
            else:
                seen.add(s[j])

            curr = j - i + 1
            maxLen = max(maxLen, curr)
            j += 1

        return maxLen