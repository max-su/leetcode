class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        chars_seen = set(s[0])
        res = 1

        for r in range(1, len(s)):
            while s[r] in chars_seen:
                chars_seen.remove(s[l])
                l += 1
            chars_seen.add(s[r])
            res = max(res, r - l + 1)
        return res
