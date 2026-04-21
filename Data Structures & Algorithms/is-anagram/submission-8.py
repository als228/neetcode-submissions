class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        sLet, tLet = {}, {}

        for i in range(len(s)):
            sLet[s[i]] = 1 + sLet.get(s[i], 0)
            tLet[t[i]] = 1 + tLet.get(t[i], 0)
        
        return sLet == tLet