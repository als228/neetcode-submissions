class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue
            else:
                l, r = 0, len(dp)-1
                while l < r:
                    m = (l+r) // 2
                    if dp[m] < nums[i]:
                        l = m+1
                    else:
                        r = m
                dp[l] = nums[i]
        
        return LIS