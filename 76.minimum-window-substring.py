import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        # tc must be an anagram of sc
        sc = collections.Counter()
        tc = collections.Counter(t)
        chars_have = 0
        chars_need = len(tc.keys())

        res_l, res_r = 0, float('inf')
        l = 0
        for r in range(len(s)):
            if s[r] in tc:
                sc[s[r]] += 1
                if sc[s[r]] == tc[s[r]]:
                    chars_have += 1

            while chars_have == chars_need:
                if r - l < res_r - res_l:
                    res_l, res_r = l, r
                if s[l] in tc:
                    if sc[s[l]] == tc[s[l]]:
                        chars_have -= 1
                    sc[s[l]] -= 1
                l += 1

        return s[res_l:res_r + 1] if res_r != float('inf') else ''
