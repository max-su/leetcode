class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                prev_index = stack.pop()[0]
                res[prev_index] = i - prev_index
            stack.append((i, n))
        return res