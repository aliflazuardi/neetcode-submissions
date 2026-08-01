class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l)//2

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: #left side sorted
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else: # left side not sorted 
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return ans