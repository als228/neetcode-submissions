class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        listDict = []

        for i, word in enumerate(strs):
            letters = {}
            for char in word:
                letters[char] = 1 + letters.get(char, 0)
            
            if letters in listDict:
                index = listDict.index(letters)
                out[index].append(strs[i])
            else:
                listDict.append(letters)
                out.append([strs[i]])

        return out