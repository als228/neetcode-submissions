class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ints = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for n in nums:
            ints[n] = 1 + ints.get(n, 0)
        for n, cnt in ints.items():
            buckets[cnt].append(n)
        
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for nums in buckets[i]:
                res.append(nums)
                if len(res) == k:
                    return res
        
        return res