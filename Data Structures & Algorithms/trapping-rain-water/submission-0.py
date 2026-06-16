class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]

        area = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                lMax = max(lMax, height[l])
                area += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                area += rMax - height[r]
        
        return area