class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]
        maxStack = [(len(temperatures)-1, temperatures.pop())]
        
        for i in range(len(temperatures) - 1, -1, -1):
            end = temperatures.pop()
            while maxStack:
                maxPair = maxStack[-1]
                if end >= maxPair[1]:
                    maxStack.pop()
                else:
                    res.append(maxPair[0] - i)
                    maxStack.append((i, end))
                    break
            if not maxStack:
                res.append(0)
                maxStack.append((i, end))
        
        res.reverse()
        return res