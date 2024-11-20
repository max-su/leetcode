import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        def add(x: int) -> None:
            while q and q[-1] < x:
                q.pop()
            q.append(x)
        def remove(x: int) -> None:
            if q and q[0] == x:
                q.popleft()

        for i in range(k):
            add(nums[i])
        
        res = [q[0]]
        for i in range(1, len(nums) - k + 1):
            remove(nums[i - 1])
            add(nums[i + k - 1])
            res.append(q[0])
        return res
