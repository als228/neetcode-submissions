class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s:
            if c in pairs:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != pairs[c]: 
                    return False
            else:
                stack.append(c)
        if len(stack) != 0: 
            return False
        return True