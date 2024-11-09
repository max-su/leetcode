import collections


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        # Union / Find
        rank = [1] * len(nums)
        parent = [i for i in range(len(nums))]
        num_to_idx = {n: i for i, n in enumerate(nums)}

        def find_parent(x):
            if x == parent[x]:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]

        def merge(a, b):
            if find_parent(a) == find_parent(b):
                return
            if rank[find_parent(a)] > rank[find_parent(b)]:
                rank[find_parent(a)] += rank[find_parent(b)]
                parent[find_parent(b)] = find_parent(a)
            else:
                rank[find_parent(b)] += rank[find_parent(a)]
                parent[find_parent(a)] = find_parent(b)

        for i, n in enumerate(nums):
            if n - 1 in num_to_idx:
                dec_idx = num_to_idx[n - 1]
                merge(dec_idx, i)
            if n + 1 in num_to_idx:
                dec_idx = num_to_idx[n + 1]
                merge(dec_idx, i)
        compressed_parent = [find_parent(i) for i in range(len(nums))]
        return max(collections.Counter(compressed_parent).values())
