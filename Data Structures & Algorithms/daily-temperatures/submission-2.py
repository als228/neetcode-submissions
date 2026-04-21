class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]
        maxStack = [(len(temperatures)-1, temperatures.pop())]
        
        while temperatures:
            end = temperatures.pop()
            while maxStack:
                maxPair = maxStack[-1]
                if end >= maxPair[1]:
                    maxStack.pop()
                else:
                    res.append(maxPair[0] - len(temperatures))
                    maxStack.append((len(temperatures), end))
                    break
            if not maxStack:
                res.append(0)
                maxStack.append((len(temperatures), end))
        
        res.reverse()
        return res