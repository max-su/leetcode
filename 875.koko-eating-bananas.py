class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(speed):
            hours_needed = 0
            for b in piles:
                hours_needed += ceil(b / speed)
            return hours_needed <= h

        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if can_eat(m):
                r = m
            else:
                l = m + 1
        return l