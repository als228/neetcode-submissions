class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def diag_attack(row, col, seq):
            for i in range(1, row+1):
                if col-i >= 0 and seq[row-i][col-i] == "Q":
                    return True
                if col+i < n and seq[row-i][col+i] == "Q":
                    return True
            return False
        
        horizontal = [False] * n
        res = []
        def btrack(row, seq):
            # base case
            if len(seq) == n:
                res.append(list(seq))
                return
            # btrack
            s = ["."] * n
            for c in range(n):
                if not horizontal[c] and not diag_attack(row, c, seq):
                    s[c] = "Q"
                    seq.append("".join(s))
                    horizontal[c] = True
                    btrack(row+1, seq)
                    horizontal[c] = False
                    seq.pop()
                    s[c] = "."
        
        btrack(0, [])
        return res