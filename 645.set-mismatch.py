class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor_all = 0
        for i in nums:
            xor_all ^= i
        for i in range(1, n + 1):
            xor_all ^= i

        lsb_xor_all = xor_all & -xor_all
        xor_set = xor_unset = 0

        for i in nums:
            # Set bit
            if lsb_xor_all & i != 0:
                xor_set ^= i
            else:
                xor_unset ^= i
        for i in range(1, n + 1):
            if lsb_xor_all & i != 0:
                xor_set ^= i
            else:
                xor_unset ^= i

        if xor_unset in nums:
            return (xor_unset, xor_set)
        return (xor_set, xor_unset)
