class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ltrs = {}
        for char in s:
            s_ltrs[char] = s_ltrs.get(char, 0) + 1
        t_ltrs = {}
        for char in t:
            t_ltrs[char] = t_ltrs.get(char, 0) + 1
        
        return s_ltrs == t_ltrs