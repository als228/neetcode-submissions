class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            for letter in word:
                res += chr(ord(letter) + 256)
            res += "Ё"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        for letter in s:
            if letter == "Ё":
                res.append(word)
                word = ""
            else:
                word += chr(ord(letter) - 256)
        
        return res