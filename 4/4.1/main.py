import operator

class Tree:
    def __init__(self, left, center, right, value):
        self.left = left
        self.center = center
        self.right = right
        self.value = value


#buffer = raw_input('Type:')


def preorderPrint(root): #
    if root == None:
        return
    print (root.value)
    preorderPrint(root.left)
    preorderPrint(root.right)


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = []
    eTree = Tree(None, None, None, None)
    pStack.append(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.left = Tree(None, None, None, None)
            pStack.append(currentTree)
            currentTree = currentTree.left
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.value = int(i)
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.value = i
            currentTree.right = Tree(None, None, None, None)
            pStack.append(currentTree)
            currentTree = currentTree.right
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(root):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_ = root.left
    right_ = root.right

    if left_ and right_:
        fn = opers[root.value]
        return fn(evaluate(left_), evaluate(right_))
    else:
        return root.value


tree = buildParseTree("( ( 2 * 3 ) - ( 4 / 1 ) ) * ( ( 4 - 2 ) / ( 5 - 3 ) )")
preorderPrint(tree)
print evaluate(tree)
