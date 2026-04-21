class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        buckets = [[] for _ in range(max(freq.values()) + 1)]
        for key, value in freq.items():
            buckets[value].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            while len(buckets[i]) != 0 and k > 0: 
                res.append(buckets[i].pop())
                k -= 1
        
        return res