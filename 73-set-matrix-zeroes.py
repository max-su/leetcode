class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Null Check
        if not matrix or not matrix[0]:
            return

        # Topmost row is for cols
        # Left row except for the topmost element is for cols
        row_zero_zero = False
        rows, cols = len(matrix), len(matrix[0])

        # Iterate through matrix, find rows/cols to set to 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Cols
                    matrix[0][j] = 0
                    # Rows
                    if i == 0:
                        row_zero_zero = True
                    else:
                        matrix[i][0] = 0

        # Set rows to 0
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        # Set cols to 0
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        # Zero out 0th col
        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0

        # Zero out 0th row
        if row_zero_zero:
            for j in range(cols):
                matrix[0][j] = 0
