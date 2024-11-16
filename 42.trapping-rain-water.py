class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0] * len(height)
        r = [0] * len(height)

        # No negative numbers, 0 suffices
        l_max = 0
        for i, n in enumerate(height):
            l_max = max(l_max, n)
            l[i] = l_max

        r_max = 0
        for i, n in reversed(list(enumerate(height))):
            r_max = max(r_max, n)
            r[i] = r_max

        area = 0
        for i, n in enumerate(height):
            l_val = l[i - 1] if i - 1 >= 0 else float("-inf")
            r_val = r[i + 1] if i + 1 < len(height) else float("-inf")
            area += max(0, min(l_val, r_val) - n)

        return area
