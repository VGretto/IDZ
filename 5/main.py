import math


class Tree:
    def __init__(self, left, center, right, value):
        self.left = left
        self.center = center
        self.right = right
        self.value = value


buffer = []

file = open("data.csv", "r")

for line in file:
    buffer.append(line)

for i in range(0, buffer.__len__(), 1):
    buffer[i] = buffer[i].split(',')

for i in range(0, buffer.__len__(), 1):
    buffer[i][4] = buffer[i][4].split('\n')[0]

print('\nDataBase:')
for i in range(0, buffer.__len__(), 1):
        print buffer[i]
print("\n")

file.close()


def Print(tr):#
    if tr == None:
        return
    print(tr.value)
    Print(tr.left)
    Print(tr.center)
    Print(tr.right)


def Gain(colon):
    low = [0, 0]
    middle = [0, 0]
    high = [0, 0]
    ret = [0, 0, 0, 0]
    for i in range(0, buffer.__len__(), 1):
        if buffer[i][colon] == "low":
            if buffer[i][4] == "no":
                low[1] = low[1] + 1
            else:
                low[0] = low[0] + 1
        elif buffer[i][colon] == "middle":
            if buffer[i][4] == "no":
                middle[1] = middle[1] + 1
            else:
                middle[0] = middle[0] + 1
        elif buffer[i][colon] == "high":
            if buffer[i][4] == "no":
                high[1] = high[1] + 1
            else:
                high[0] = high[0] + 1
    if low[0] == 0 or low[1] == 0:
        ret[0] = 0
    else:
        ret[0] = -low[0]/(low[0]+low[1]) * math.log(float(low[0])/float((low[0]+low[1])), 2)-low[1]/(low[0]+low[1]) * math.log(float(low[1])/float((low[0]+low[1])), 2)
    if middle[0] == 0 or middle[1] == 0:
        ret[1] = 0
    else:
        ret[1] = -middle[0] / (middle[0] + middle[1]) * math.log(float(middle[0]) / float((middle[0] + middle[1])), 2) - middle[1] / (middle[0] + middle[1]) * math.log(float(middle[1]) / float((middle[0] + middle[1])), 2)
    if high[0] == 0 or high[1] == 0:
        ret[2] = 0
    else:
        ret[2] = -high[0] / (high[0] + high[1]) * math.log(float(high[0]) / float((high[0] + high[1])), 2) - high[1] / (high[0] + high[1]) * math.log(float(high[1]) / float((high[0] + high[1])), 2)
    tmp0 = low[0]+middle[0]+high[0]
    tmp1 = low[1]+middle[1]+high[1]
    ret[3] = -tmp0 / (tmp0 + tmp1) * math.log(float(tmp0) / float((tmp0 + tmp1)), 2) - tmp1 / (tmp0 + tmp1) * math.log(float(tmp1) / float((tmp0 + tmp1)), 2)
    #print low, middle, high, ret[3]
    E = float(low[0]+low[1]) / float(tmp0+tmp1) * ret[0] + float((middle[0]+middle[1])) / float((tmp0+tmp1)) * ret[1] + float((high[0]+high[1])) / float((tmp0+tmp1)) * ret[2]
    #print E
    G = ret[3]-E
    print G
    return G


it0 = [Gain(0), Gain(1), Gain(2), Gain(3)]
it1 = [0, 1, 2, 3]
for i in range(0, 2, 1):
    for j in range(0, 2, 1):
        if it0[j] > it0[j+1]:
            tmp = it0[j]
            it0[j] = it0[j+1]
            it0[j+1] = tmp
            tmp = it1[j]
            it1[j] = it1[j + 1]
            it1[j + 1] = tmp


it1.reverse()
print it1

root = Tree(None, None, None, "#")
tmp = root
for i in range(0, buffer.__len__(), 1):
    tmp = root
    #print '----'
    for j in range(0, 4, 1):
        #print buffer[i][it1[j]]
        if j == 3:
            k = buffer[i]
        else:
            k = '|'
        if buffer[i][it1[j]] == 'low':
            if tmp.left:
                tmp = tmp.left
            else:
                tmp.left = Tree(None, None, None, k)
                tmp = tmp.left
        elif buffer[i][it1[j]] == 'middle':
            if tmp.center:
                tmp = tmp.center
            else:
                tmp.center = Tree(None, None, None, k)
                tmp = tmp.center
        elif buffer[i][it1[j]] == 'high':
            if tmp.right:
                tmp = tmp.right
            else:
                tmp.right = Tree(None, None, None, k)
                tmp = tmp.right


#Print(root)

print root.right.right.left.right.value
