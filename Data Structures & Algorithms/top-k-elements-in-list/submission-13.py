class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        freq_map = {}

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        
        for num, freq in freq_map.items():
            heapq.heappush(minheap, (freq, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        return list(num for freq, num in minheap)