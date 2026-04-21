class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        # either way, maximum might be a result
        res = r

        # we do <= and not < because min speed often
        # is when l == r, so we need to assign this to res
        while l <= r:
            if r == 0: break
            mid = l + math.ceil((r-l)/2)
            numDivisions = 0

            for num in piles:
                numDivisions += math.ceil(num / mid)
            
            # if speed too small, then definitely need to increase left
            if numDivisions > h:
                l = mid + 1
            # if speed too high (or even numDivisions == h,
            # but mid can be smaller), then decrease right 
            # but keep track of current res
            else:
                res = mid
                r = mid-1

        return res