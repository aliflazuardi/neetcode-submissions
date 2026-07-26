class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hashmap method
        group_map = defaultdict(int)
        ans = 0

        for num in nums:
            if not group_map[num]:
                group_map[num] = group_map[num-1] + 1 + group_map[num+1]
                group_map[num - group_map[num - 1]] = group_map[num]
                group_map[num + group_map[num + 1]] = group_map[num]
                ans = max(ans, group_map[num])

        return ans