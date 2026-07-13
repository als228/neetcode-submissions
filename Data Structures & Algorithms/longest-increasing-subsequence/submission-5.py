class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = 1
        seq = [nums[0]]

        for num in nums:
            if num > seq[-1]:
                seq.append(num)
                LIS += 1
            else:
                l, r = 0, len(seq)-1
                while l < r:
                    m = (l+r) // 2
                    if num > seq[m]:
                        l = m+1
                    else:
                        r = m
                seq[r] = num
        
        return LIS