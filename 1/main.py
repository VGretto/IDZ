#825*+132*+4-/

#colecting data
buffer = raw_input('type polish word to process:')

#buffers
stack = []

#functions
def compute(a, b, c):
    if c == '*':
        tmp = a * b
    elif c == '/':
        tmp = a / b
    elif c == '+':
        tmp = a + b
    elif c == '-':
        tmp = a - b
    elif c == '^':
        tmp = a ** b


    stack[stack.__len__() - 2] = tmp
    stack.pop()
    print(stack)

#processing data

for index in buffer:
    z = stack.__len__()
    if index == '*':
        compute(float(stack[z-2]), float(stack[z-1]), '*')
    elif index == '/':
        compute(float(stack[z - 2]), float(stack[z - 1]), '/')
    elif index == '+':
        compute(float(stack[z - 2]), float(stack[z - 1]), '+')
    elif index == '-':
        compute(float(stack[z - 2]), float(stack[z - 1]), '-')
    elif index == '^':
        compute(float(stack[z - 2]), float(stack[z - 1]), '^')
    else:
        stack.append(index)
        print(stack)


stack.pop()