def makeGoodStr(string: str) -> str:
    stack = []
    for char in string:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

print(makeGoodStr('sSstAaackKCck'))