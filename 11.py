class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        l, r = 0, len(height) - 1
        while l < r:
            width = r - l
            h = min(height[l], height[r])
            area = width * h
            max_area = max(max_area, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area
