class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        
        heapq.heapify(stones)
        while len(stones) > 1:
            max_heavy = abs(heapq.heappop(stones))
            max_heavy_2 = abs(heapq.heappop(stones))
            if max_heavy > max_heavy_2: 
                heapq.heappush(stones, -1*(max_heavy - max_heavy_2))
        return abs(stones[0]) if stones else 0