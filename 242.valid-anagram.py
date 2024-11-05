import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mp = collections.Counter(s)
        t_mp = collections.Counter(t)
        return s_mp == t_mp
