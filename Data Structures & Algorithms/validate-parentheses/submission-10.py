class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '[':']', '{':'}'}
        
        # quick false return
        if (len(s)%2 != 0):
            return False
        # loop to iterate
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack or pairs[stack.pop()] != char:
                    return False
        return not stack