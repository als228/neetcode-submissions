class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            mid = (l+r)//2
            if nums[r] > nums[mid]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid
            else:
                res = nums[r]
                break

        return res