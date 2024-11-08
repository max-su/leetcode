class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Consume an entire element
            # Number of characters of string
            # '#'
            # string content
            size = 0
            while s[i].isnumeric():
                size *= 10
                size += int(s[i])
                i += 1
            # Skip #
            i += 1
            # Build the string
            sb = []
            for _ in range(size):
                sb.append(s[i])
                i += 1
            res.append("".join(sb))
        return res
