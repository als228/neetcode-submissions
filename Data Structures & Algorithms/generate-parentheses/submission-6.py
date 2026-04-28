class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combo = []

        def dfw(op, cl):
            if op == 0 and cl == 0:
                res.append("".join(combo))
                return

            if op > 0:
                combo.append("(")
                dfw(op-1, cl)
                combo.pop()
            if cl > op:
                combo.append(")")
                dfw(op, cl-1)
                combo.pop()

        dfw(n, n)
        return res