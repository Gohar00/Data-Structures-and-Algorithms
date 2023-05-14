class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
         result = 0
         digits = []
         for digit in num:
            result = result * 10 + digit
         result += k
         while result > 0:
            digit = result % 10
            digits.insert(0, digit)
            result //= 10
         return digits
