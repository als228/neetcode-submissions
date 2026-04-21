class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLet = {}
        tLet = {}

        for char in s:
            if sLet.get(char) is not None:
                sLet[char] = sLet.get(char) + 1
            else:
                sLet[char] = 1
        for char in t:
            if tLet.get(char) is not None:
                tLet[char] = tLet.get(char) + 1
            else:
                tLet[char] = 1
        
        return sLet == tLet