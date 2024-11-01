class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1

        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        a = nums[0]
        while a != slow:
            a = nums[a]
            slow = nums[slow]

        return a
