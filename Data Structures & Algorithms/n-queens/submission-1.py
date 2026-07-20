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
        diag1 = set()
        diag2 = set()
        res = []
        def btrack(row, seq):
            # base case
            if len(seq) == n:
                res.append(list(seq))
                return
            # btrack
            s = ["."] * n
            for c in range(n):
                if not horizontal[c] and row+c not in diag1 and row-c not in diag2:
                    s[c] = "Q"
                    seq.append("".join(s))
                    horizontal[c] = True
                    diag1.add(row+c)
                    diag2.add(row-c)
                    btrack(row+1, seq)
                    diag1.remove(row+c)
                    diag2.remove(row-c)
                    horizontal[c] = False
                    seq.pop()
                    s[c] = "."
        
        btrack(0, [])
        return res