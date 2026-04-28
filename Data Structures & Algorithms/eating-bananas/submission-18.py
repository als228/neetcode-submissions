class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = math.ceil((l+r) / 2)
            num_div = 0

            for num in piles:
                num_div += math.ceil(num / mid)
            
            if num_div > h:
                l = mid+1
            else:
                res = mid
                r = mid-1
        
        return res