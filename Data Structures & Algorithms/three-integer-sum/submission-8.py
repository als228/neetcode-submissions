class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            # no more sums will result in 0
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1

            # loop
            while l < r:
                if nums[l]+nums[r]+num == 0:
                    res.append([nums[l], nums[r], num])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l]+nums[r]+num < 0:
                    l += 1
                else:
                    r -= 1

        return res