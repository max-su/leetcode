class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Move nums1 to the back
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]

        # 0 1 2 3 4 5
        # 6 - 3
        nums1_idx = len(nums1) - m
        nums2_idx = merge_idx = 0

        while nums1_idx < len(nums1) or nums2_idx < n:
            val1 = nums1[nums1_idx] if nums1_idx < len(nums1) else float("inf")
            val2 = nums2[nums2_idx] if nums2_idx < len(nums2) else float("inf")
            if val1 < val2:
                nums1[merge_idx] = val1
                nums1_idx += 1
            else:
                nums1[merge_idx] = val2
                nums2_idx += 1
            merge_idx += 1
