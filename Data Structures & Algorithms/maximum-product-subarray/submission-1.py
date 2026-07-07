class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min = cur_max = 1

        for n in nums:
            tmp = n * cur_max
            cur_max = max(n, n*cur_min, n*cur_max)
            cur_min = min(n, n*cur_min, tmp)
            res = max(res, cur_max)

        return res