class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row0 = False

        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row0 = True
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for r in range(n):
                matrix[r][0] = 0
        
        if row0:
            for c in range(m):
                matrix[0][c] = 0