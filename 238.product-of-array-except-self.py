class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = right_prod = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= left_prod
            left_prod *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]

        return res
