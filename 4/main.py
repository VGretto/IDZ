import time

class Tree:
    def __init__(self, left, center, right, value):
        self.left = left
        self.center = center
        self.right = right
        self.value = value


#t = Tree(Tree("a", None), Tree(None, "d"))

#colecting data
#buffer = raw_input('type polish word to process:')
#c = len(buffer)


#
tree_a = Tree(Tree(Tree(None, None, None, "c"), None, Tree(None, None, None, "d"), "b"), None, Tree(Tree(None, None, None, "f"), Tree(None, None, None, "g"), Tree(None, None, None, "h"), "e"), "a")
tree_b = Tree(Tree(Tree(None, None, None, "c"), Tree(None, None, None, "d"), Tree(None, None, None, "b"), "f"), None, Tree(Tree(None, None, None, "g"), None, Tree(None, None, None, "h"), "e"), "a")


def reversePrint(root):#
    if root == None:
        return
    reversePrint(root.left)
    reversePrint(root.center)
    reversePrint(root.right)
    print (root.value)


def getMil():
    return int(round(time.time() * 1000))


a = getMil()
reversePrint(tree_a)
b = getMil()
print a,b

a = getMil()
reversePrint(tree_b)
b = getMil()
print a,b
