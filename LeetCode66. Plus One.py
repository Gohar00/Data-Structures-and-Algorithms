class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        result = 0
        for num in digits:
            result = result * 10 + num
        result = result + 1
        
        lst = []
        while result != 0:
            dig = result % 10
            result = result // 10
            lst.append(dig)
        return reversed(lst)