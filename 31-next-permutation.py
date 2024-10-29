class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find j
        j = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                j = i
                break

        # 9 6 3
        if j == -1:
            nums.reverse()
            return

        # Find k
        # k is guaranteed to exist
        k = -1
        for i in range(len(nums) - 1, j, -1):
            if nums[i] > nums[j]:
                k = i
                break

        nums[j], nums[k] = nums[k], nums[j]
        nums[j + 1 :] = sorted(nums[j + 1 :])
