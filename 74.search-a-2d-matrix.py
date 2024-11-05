class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # Search for row, bisect
        l, r = 0, m - 1
        while l < r:
            m = (l + r) // 2
            if target <= matrix[m][-1]:
                r = m
            else:
                l = m + 1

        if l > r:
            return False

        row_idx = l

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row_idx][m] == target:
                return True
            elif matrix[row_idx][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False
