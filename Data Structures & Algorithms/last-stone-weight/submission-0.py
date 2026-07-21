class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            z = x - y
            if z != 0:
                heapq.heappush(heap, -1 * abs(z))
            if len(heap) == 1:
                return -1 * heap[0]

        return 0