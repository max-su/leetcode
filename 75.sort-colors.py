class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

        r = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
