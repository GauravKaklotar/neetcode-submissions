class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def apply(op, b, a):
            match op:
                case '+':
                    return a + b
                case '-':
                    return a - b
                case '*':
                    return a * b
                case '/':
                    return int(a / b)

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                stack.append(
                    apply(token, stack.pop(), stack.pop())
                )

        return stack[0]