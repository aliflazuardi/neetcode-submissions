class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = 1000

        while l <= r:
            m = l + (r - l)//2
            ans = min(ans, nums[m])

            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1


        return ans