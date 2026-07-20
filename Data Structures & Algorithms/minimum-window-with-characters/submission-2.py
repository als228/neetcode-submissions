class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # what chars we need
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        # comparison
        need = len(countT)
        have = 0
        # storing res
        res = []
        window = {}
        l = 0

        for r in range(len(s)):
            # update the window
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while need == have:
                if not res or res[1] - res[0] > r-l:
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1]+1] if res else ""