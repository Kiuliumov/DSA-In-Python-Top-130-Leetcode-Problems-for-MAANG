class Solution:
    def isValid(self, s: str) -> bool:
        validity_map = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []

        for p in s:
            if p in validity_map:
                if not stack or stack.pop() != validity_map[p]:
                    return False
            else:
                stack.append(p)

        return len(stack) == 0