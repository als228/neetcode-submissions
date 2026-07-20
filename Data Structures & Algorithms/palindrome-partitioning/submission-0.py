class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start, end):
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
        
        res = []
        def btrack(index, seq):
            # base case
            if index == len(s):
                res.append(list(seq))
                return
            # keep btrack
            for i in range(index, len(s)):
                if isPalindrome(index, i):
                    seq.append(s[index:i+1])
                    btrack(i+1, seq)
                    seq.pop()
        
        btrack(0, [])
        return res