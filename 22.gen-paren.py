class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(l: int, r: int, path) -> None:
            if l == r == n:
                res.append(''.join(path))
                return
            if l < n:
                path.append('(')
                backtrack(l + 1, r, path)
                path.pop()
            #(()
            if l > r:
                path.append(')')
                backtrack(l, r + 1, path)
                path.pop()
            
        backtrack(0, 0, [])
        return res