class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1 pass to find min
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        m = l
        # 2 pass
        def binary(l, r):
            while l <= r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return -1
        
        res = binary(0, m-1)
        if res != -1:
            return res
        else:
            return binary(m, len(nums)-1)