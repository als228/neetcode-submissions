class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        def btrack(index, seq):
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                seq.append(nums[i])
                res.append(list(seq))
                btrack(i+1, seq)
                seq.pop()
        
        btrack(0, [])
        return res