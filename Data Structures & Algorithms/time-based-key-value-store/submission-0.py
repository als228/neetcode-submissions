class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        self.keyVals = self.timeMap[key]
        self.res = ""
        self.l, self.r = 0, len(self.keyVals)-1
        while self.l <= self.r:
            self.mid = (self.l + self.r) // 2
            if self.keyVals[self.mid][0] > timestamp:
                self.r = self.mid - 1
            else:
                self.l = self.mid + 1
                self.res = self.keyVals[self.mid][1]
        
        return self.res