''' function to identify if parenthesis are in order '''


def isValidParenthesis(s: str) -> bool:
    stack = []
    left = ['{', "[", '(']
    right = ['}', "]", ')']

    for n in s:
        if n in left:
            stack.append(n)
        elif n in right:
            if len(stack) <= 0 or left.index(stack.pop()) != right.index(n):
                return False

    return len(stack) == 0


if __name__ == '__main__':
    isValidParenthesis("[{()}]")
