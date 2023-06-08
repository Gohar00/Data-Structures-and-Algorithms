class Solution:
    def countNegatives(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < 0:
                    count += 1
        return count