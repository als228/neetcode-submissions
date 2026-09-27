class Solution:
    def trap(self, height: List[int]) -> int:
        # assign local pointers
        l, r = 0, len(height)-1
        while l < r and height[l+1] >= height[l]:
            l += 1
        while l < r and height[r-1] >= height[r]:
            r -= 1

        # assign global pointers
        lMax, rMax = height[l], height[r]
        res = 0

        while l < r:
            # update pointers
            if height[l] < height[r]:
                l += 1
                if height[l] >= lMax:
                    lMax = height[l]
                else:
                    res += min(lMax, rMax) - height[l]
            else:
                r -= 1
                if height[r] >= rMax:
                    rMax = max(rMax, height[r])
                else:
                    res += min(lMax, rMax) - height[r]
        
        return res