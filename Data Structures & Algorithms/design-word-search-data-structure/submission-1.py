class Trie:
    def __init__(self):
        self.ends = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.ends = True

    def helper(self, trie, word, index):
        # base case
        if index >= len(word):
            return trie.ends
        # dfs
        cur = trie
        for i in range(index, len(word)):
            if word[i] == '.':
                for trie in cur.children.values():
                    if self.helper(trie, word, i+1):
                        return True
                return False
            else:
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
        return cur.ends

    def search(self, word: str) -> bool:
        return self.helper(self.root, word, 0)