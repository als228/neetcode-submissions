class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastDigit = digits[len(digits)-1]
        if lastDigit != 9:
            digits[len(digits)-1] += 1
        else:
            i = len(digits)-1
            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i -= 1
            if i >= 0:
                digits[i] += 1
            elif i < 0:
                digits.insert(0, 1)
        return digits