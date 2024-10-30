class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = max_sum = nums[0]
        for r in range(1, len(nums)):
            dp = max(dp + nums[r], nums[r])
            max_sum = max(max_sum, dp)
        return max_sum
