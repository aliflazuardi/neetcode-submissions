class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, f in freq_map.items():
            freq[f].append(n)
        
        c = 0
        p = len(nums)
        res = []
        while c < k:
            if freq[p]:
                for e in freq[p]:
                    res.append(e)
                    c += 1
            p -= 1

        return res
