class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[0 for _ in range(j)] for j in range(1, numRows + 1)]
        res[0][0] = 1
        for i in range(1, numRows):
            row_size = i + 1
            for j in range(row_size):
                # Top Left
                res[i][j] += res[i - 1][j - 1] if j - 1 >= 0 else 0
                # Top
                res[i][j] += res[i - 1][j] if j < len(res[i - 1]) else 0
        return res
