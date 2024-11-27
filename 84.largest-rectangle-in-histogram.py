class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # (Index, Height) o
        max_area = 0
        left_xy = []
        heights.append(0)
        for right_x, right_h in enumerate(heights):
            curr_x = right_x
            # 2, 1
            while left_xy and left_xy[-1][1] > right_h:
                left_x, left_y = left_xy.pop()
                curr_x = left_x

                # Calculate the biggest rectangle rooted at the popped lext_xy side
                max_area = max((right_x - left_x) * left_y, max_area)
            left_xy.append((curr_x, right_h))
        return max_area