import math
def evalRPN(tokens: list[str]) -> int:
    stack = []
    print(tokens)
    for e in tokens:
        if e in {'+', '-', '*', '/'}:
            second = stack.pop()
            first = stack.pop()
            stack.append(eval(f"{first} {'//' if e == '/' else e} {second}"))
        else:
            stack.append(e)
    return stack[0]


evalRPN(tokens=['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])