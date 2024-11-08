import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def dict_to_s(mp):
            c_freq = sorted(list(mp.items()), key=lambda x: x[0])
            res = []
            for c, freq in c_freq:
                res.append(c)
                res.append(str(freq))
            return ",".join(res)

        s_to_anagrams = collections.defaultdict(list)
        for s in strs:
            hsh = dict_to_s(collections.Counter(s))
            s_to_anagrams[hsh].append(s)
        return list(s_to_anagrams.values())
