class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "-+*/":
                l = stack.pop()
                p = stack.pop()

                if i == "+":
                    stack.append(p + l)
                if i == "-":
                    stack.append(p - l)
                if i == "*":
                    stack.append(p * l)
                if i == "/":
                    stack.append(int(p / l))
            else:
                stack.append(int(i))

        return stack.pop()