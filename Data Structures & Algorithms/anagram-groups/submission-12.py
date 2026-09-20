class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            ltrs = [0 for _ in range(26)]
            for c in word:
                index = ord(c) - ord('a')
                ltrs[index] += 1
            
            anagrams[tuple(ltrs)].append(word)
        
        return list(anagrams.values())