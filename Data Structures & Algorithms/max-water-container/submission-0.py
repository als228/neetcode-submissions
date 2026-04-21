class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights)-1
        while l < r:
            lHeight, rHeight = heights[l], heights[r]
            area = max(area, (r-l) * min(lHeight, rHeight))
            if lHeight > rHeight:
                while l < r and rHeight >= heights[r]: 
                    r -= 1
            else:
                while l < r and lHeight >= heights[l]: 
                    l += 1

        return area