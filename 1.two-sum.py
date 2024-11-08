class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addend_to_idx = {}
        for i, n in enumerate(nums):
            if target - n in addend_to_idx:
                return [addend_to_idx[target - n], i]
            addend_to_idx[n] = i

        return (-1, -1)
