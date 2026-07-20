class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def btrack(hashset, seq):
            if len(hashset) == len(nums):
                res.append(list(seq))
                return
            for i in range(len(nums)):
                if nums[i] not in hashset:
                    hashset.add(nums[i])
                    seq.append(nums[i])
                    btrack(hashset, seq)
                    hashset.remove(nums[i])
                    seq.pop()

        btrack(set(), [])
        return res