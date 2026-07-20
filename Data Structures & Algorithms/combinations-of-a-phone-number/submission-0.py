class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ltrs = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"],
                "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"],
                "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        
        res = []
        def btrack(index, seq):
            if index == len(digits):
                res.append("".join(seq))
                return
            for c in ltrs[digits[index]]:
                seq.append(c)
                btrack(index+1, seq)
                seq.pop()
        
        btrack(0, [])
        return res