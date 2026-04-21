class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        minIndex = 0
        ltrs = set()

        for i, char in enumerate(s):
            if char not in ltrs:
                ltrs.add(char)
            else:
                while (char != s[minIndex]):
                    ltrs.remove(s[minIndex])
                    minIndex += 1
                minIndex += 1
            
            maxL = max(maxL, i - minIndex + 1)
        return maxL