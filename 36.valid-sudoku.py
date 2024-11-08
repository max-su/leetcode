class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(A):
            # All elements are . or [1..9]
            if not all(x == "." or x.isnumeric() for x in A):
                return False
            seen_nums = set()
            for n in A:
                if n == ".":
                    continue
                elif n in seen_nums:
                    return False
                seen_nums.add(n)
            return True

        # Rows
        for row in board:
            if not is_valid(row):
                return False

        # Cols
        for j in range(9):
            col = []
            for i in range(9):
                col.append(board[i][j])
            if not is_valid(col):
                return False

        # Squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                for ia in range(3):
                    for ja in range(3):
                        row = i + ia
                        col = j + ja
                        v = board[row][col]
                        square.append(v)

                if not is_valid(square):
                    return False
        return True
