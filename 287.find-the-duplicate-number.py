class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        curr = nums[0]
        while True:
            curr = nums[curr]
            slow = nums[slow]
            if slow == curr:
                return slow
        return slow