class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            while i > 0 and i < n and nums[i] == nums[i-1]: 
                i += 1
            l = i + 1
            r = n - 1

            while l < r:
                if nums[i]+nums[l]+nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                if nums[i]+nums[l]+nums[r] < 0:
                    l += 1
                if nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
            
            i += 1


        return ans