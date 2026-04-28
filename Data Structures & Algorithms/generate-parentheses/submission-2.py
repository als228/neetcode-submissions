class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfw(rem_brackets, rem_clos, string):
            if rem_brackets > rem_clos:
                return
            if rem_brackets == 0 and rem_clos == 0:
                res.append(string[:])
                return

            if rem_brackets > 0:
                string += "("
                dfw(rem_brackets-1, rem_clos, string)
                string = string[:len(string)-1]
            if rem_clos > 0:
                string += ")"
                dfw(rem_brackets, rem_clos-1, string)
                string = string[:len(string)-1]

        dfw(n, n, "")
        return res