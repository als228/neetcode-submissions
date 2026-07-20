class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def btrack(index, remainder, seq):
            if remainder == 0:
                res.append(list(seq))
                return
            if remainder < 0:
                return
            for i in range(index, len(candidates)):
                if i-1 >= index and candidates[i] == candidates[i-1]:
                    continue
                seq.append(candidates[i])
                btrack(i+1, remainder-candidates[i], seq)
                seq.pop()

        btrack(0, target, [])
        return res