#usr/bin/env python3
# python doesn't complie, but rather interprets the commands in the file at runtime

def add(a, b):
    return a + b

def sub(a, b):
    return b - a

def mult(a, b):
    return a * b

operators = {
        '+': add,
        '-': sub,
        '*': mult,
        }

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)

    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':
    main()


