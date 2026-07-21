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

    def search(self, word: str) -> bool:
        def dfs(index, trie):
            # base case
            if index == len(word):
                return trie.ends
            # iteration
            if word[index] == '.':
                for child_trie in trie.children.values():
                    if dfs(index+1, child_trie):
                        return True
                return False
            else:
                if word[index] not in trie.children:
                    return False
                return dfs(index+1, trie.children[word[index]])
        
        return dfs(0, self.root)
