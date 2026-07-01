class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        def solve(i, j, k):

            if (
                i < 0 or
                i >= rows or
                j < 0 or
                j >= cols or
                board[i][j] != word[k]
            ):
                return False

            if k == len(word)-1:
                return True

            temp = board[i][j]
            board[i][j] = "#"

            for dr, dc in directions:
                if solve(i+dr, j+dc, k+1):
                    return True

            board[i][j] = temp

            return False


        for i in range(rows):
            for j in range(cols):

                if solve(i, j, 0):
                    return True

        return False