class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ints = {}
        for n in nums:
            ints[n] = 1 + ints.get(n, 0)
        
        res = []
        for i in range(k):
            max_key = max(ints, key=ints.get)
            res.append(max_key)
            ints[max_key] = 0
        return res