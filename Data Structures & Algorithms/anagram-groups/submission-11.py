class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        freq = defaultdict(list)

        for word in strs:
            ltrs = [0 for _ in range(26)]
            for letter in word:
                ltrs[ord(letter) - 97] += 1

            freq[tuple(ltrs)].append(word)

        for array in freq.values():
            res.append(array)
        return res