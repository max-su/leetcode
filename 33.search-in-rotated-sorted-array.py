class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            l, r = 0, len(nums) - 1
            # Find index of rotation
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l
        def b_search(nums: List[int], l: int, r: int) -> int:
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        rot_idx = findMin(nums)
        if rot_idx == 0:
            return b_search(nums, 0, len(nums) - 1)
        a = b_search(nums, 0, rot_idx - 1)
        b = b_search(nums, rot_idx, len(nums) - 1)
        if a != -1:
            return a
        elif b != -1:
            return b
        return -1