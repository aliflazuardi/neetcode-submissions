class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #  Hashset method

        numSet = set(nums)
        ans = 0
        
        for num in numSet:
            if num - 1 in numSet:
                continue
            length = 1
            nextNum = num + 1
            while nextNum in numSet:
                length += 1
                nextNum += 1
            ans = max(ans, length)

        return ans
