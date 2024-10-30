class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for k in range((n + 1) // 2):
            # Odd and last border is a single 1x1 element
            if n % 2 == 1 and (n + 1) // 2 - 1 == k:
                continue

            for i in range(k, n - k - 1):
                tl_x, tl_y = (k, i)
                tr_x, tr_y = (i, n - k - 1)
                br_x, br_y = (n - k - 1, n - i - 1)
                bl_x, bl_y = (n - i - 1, k)

                tl_val, tr_val, br_val, bl_val = (
                    matrix[tl_x][tl_y],
                    matrix[tr_x][tr_y],
                    matrix[br_x][br_y],
                    matrix[bl_x][bl_y],
                )

                (
                    matrix[tl_x][tl_y],
                    matrix[tr_x][tr_y],
                    matrix[br_x][br_y],
                    matrix[bl_x][bl_y],
                ) = (bl_val, tl_val, tr_val, br_val)
