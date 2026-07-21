class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        seen = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in seen.keys():
                return [seen[pair], i]
            
            if nums[i] not in seen.keys():
                seen[nums[i]] = i

        return [0, 1]

        