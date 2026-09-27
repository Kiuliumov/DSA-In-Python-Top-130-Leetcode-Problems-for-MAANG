class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        operators = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
                continue

            b = stack.pop()
            a = stack.pop()

            if t == "+":
                result = a + b
            elif t == "-":
                result = a - b
            elif t == "*":
                result = a * b
            else:
                result = int(a / b)

            stack.append(result)

        return stack[0]