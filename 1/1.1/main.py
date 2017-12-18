import random

matrix = []

x = raw_input('matrix dimensions?\nx:')
y = raw_input('y:')

for i in range(0, int(x), 1):
    matrix.append([])
    for j in range(0, int(y), 1):
        matrix[i].append(random.randrange(1, 9))

for i in range(1,20,1):
    matrix[random.randrange(0, 2)][random.randrange(0, len(matrix[0]))] = 0


while 1:
    for i in range(0, len(matrix)):
        print(matrix[i])

    print('what can i do with matrix?\n1.Element print\n2.Element edit\n3.Element calculate\n4.Vector calculate')
    ans = raw_input('answer:')


    if ans == '1':
        x = raw_input('x:')
        y = raw_input('y:')
        print(matrix[int(x)-1][int(y)-1])
    elif ans == '2':
        x = raw_input('x:')
        y = raw_input('y:')
        print(matrix[int(x) - 1][int(y) - 1])
        z = raw_input('replace with?:')
        matrix[int(x) - 1][int(y) - 1] = int(z)
    elif ans == '3':
        x = raw_input('x:')
        y = raw_input('y:')
        print(matrix[int(x) - 1][int(y) - 1])
        z = raw_input('do what? * / + - ^:')
        u = raw_input('do with? number:')
        if z == '*':
            matrix[int(x) - 1][int(y) - 1] = matrix[int(x) - 1][int(y) - 1] * int(u)
        elif z == '/':
            matrix[int(x) - 1][int(y) - 1] = matrix[int(x) - 1][int(y) - 1] / int(u)
        elif z == '+':
            matrix[int(x) - 1][int(y) - 1] = matrix[int(x) - 1][int(y) - 1] + int(u)
        elif z == '-':
            matrix[int(x) - 1][int(y) - 1] = matrix[int(x) - 1][int(y) - 1] - int(u)
        elif z == '^':
            matrix[int(x) - 1][int(y) - 1] = matrix[int(x) - 1][int(y) - 1] ** int(u)

    elif ans == '4':
        x = raw_input('x:')
        print(matrix[int(x) - 1])
        z = raw_input('do what? * / + - ^:')
        u = raw_input('do with? number:')
        if z == '*':
            for t in range(0, len(matrix[0]), 1):
                matrix[int(x) - 1][t] = matrix[int(x) - 1][t] * int(u)
        elif z == '/':
            for t in range(0, len(matrix[0]), 1):
                matrix[int(x) - 1][t] = matrix[int(x) - 1][t] / int(u)
        elif z == '+':
            for t in range(0, len(matrix[0]), 1):
                matrix[int(x) - 1][t] = matrix[int(x) - 1][t] + int(u)
        elif z == '-':
            for t in range(0, len(matrix[0]), 1):
                matrix[int(x) - 1][t] = matrix[int(x) - 1][t] - int(u)
        elif z == '^':
            for t in range(0, len(matrix[0]), 1):
                matrix[int(x) - 1][t] = matrix[int(x) - 1][t] ** int(u)