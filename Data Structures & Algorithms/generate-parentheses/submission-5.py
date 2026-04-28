class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfw(op, cl, string):
            if op == 0 and cl == 0:
                res.append(string[:])
                return

            if op > 0:
                string += "("
                dfw(op-1, cl, string)
                string = string[:len(string)-1]
            if cl > op:
                string += ")"
                dfw(op, cl-1, string)
                string = string[:len(string)-1]

        dfw(n, n, "")
        return res