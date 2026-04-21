class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '[':']', '{':'}'}
        
        # quick false return
        if (len(s)%2 != 0):
            return False
        # loop to iterate
        stack = []
        for char in s:
            if char in pairs.keys():
                stack.append(char)
            else:
                if len(stack) != 0:
                    elem = stack.pop()
                    if pairs[elem] != char:
                        return False
                else:
                    return False
        return len(stack) == 0