class Solution:
    SPACING = 16
    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            for c in word:
                out += chr(ord(c) + self.SPACING)
            out += "&"
        
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        word = ""
        for c in s:
            if c == "&":
                out.append(word)
                word = ""
            else:
                word += chr(ord(c) - self.SPACING)
        
        return out