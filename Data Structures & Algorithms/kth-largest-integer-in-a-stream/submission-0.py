class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        n = len(nums)
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

        if k < n:
            for i in range(n - k):
                smallest = heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        if len(self.heap) == 0 or len(self.heap) < self.k or val > self.heap[0]:
            heapq.heappush(self.heap, val)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)