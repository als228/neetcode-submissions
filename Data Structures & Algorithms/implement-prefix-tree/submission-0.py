class PrefixTree:

    def __init__(self):
        self.root = {}
        self.root['end'] = False

    def insert(self, word: str) -> None:
        map = self.root
        for c in word:
            if c in map:
                map = map[c]
            else:
                map[c] = {}
                map = map[c]
                map['end'] = False
        map['end'] = True

    def search(self, word: str) -> bool:
        map = self.root
        for c in word:
            if c in map:
                map = map[c]
            else:
                return False
        return map['end']

    def startsWith(self, prefix: str) -> bool:
        map = self.root
        for c in prefix:
            if c in map:
                map = map[c]
            else:
                return False
        return True