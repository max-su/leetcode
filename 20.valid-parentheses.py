class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        r_to_l = {')':'(', ']': '[', '}': '{'}
        for c in s:
            # if c in r_to_l:
            #     if not stack or stack.pop() != r_to_l[c]:
            #         return False
            if c not in r_to_l:
                stack.append(c)
            elif (not stack or stack.pop() != r_to_l[c]):
                return False
        return not stack