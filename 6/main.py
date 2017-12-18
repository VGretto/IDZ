trans = ['T100', 'T200', 'T300', 'T400']
elems = [['A', 'B', 'C', 'E'], ['A', 'B', 'C', 'D', 'K'], ['A', 'C', 'D', 'K'], ['A', 'B', 'C']]
todo = []
ms = 60
mc = 70

for i in range(0, elems.__len__()):
    for j in range(0, elems[i].__len__()):
        if todo.count(elems[i][j]) == 0:
            todo.append(elems[i][j])

todo.sort()


def supp(elem):
    c = []
    q = []
    for i in range(0, elems.__len__()):
        for j in range(0, elem.__len__()):
            #print i, j, elems[i].count(elem[j])
            c.append(elems[i].count(elem[j]))
    for k in range(0, c.__len__(), elem.__len__()):
        con = 1
        for h in range(k, k+elem.__len__()):
            if c[h] == 0:
                con = 0
        if con == 1:
            q.append(1) # maybe I should use q=q+1 and dont count it on return, but....
        #else:
        #    q.append(0)
    return int(float(q.count(1))/float(trans.__len__())*100)


def conf(supp1, supp2):
    return (float(supp2)/float(supp1))*100


#supp(['A', 'B', 'C'])
for i in range(0, todo.__len__()):
    if supp(todo[i]) >= ms:
        print todo[i], str(supp(todo[i])) + "%"
        for j in range(0, todo.__len__()):
            if todo[i] != todo[j]:
                print str(todo[i])+" => "+str(todo[j])+" : "+str(conf(supp(todo[i]), supp(todo[j])))+"%"

for i in range(0, todo.__len__()):
    for j in range(i+1, todo.__len__()):
        out = []
        for k in range(0, i):
            out.append(todo[k])
        out.append(todo[i])
        out.append(todo[j])
        if supp(out) >= ms:
            print out, str(supp(out))+"%"
            for j in range(0, todo.__len__()):
                if not out.count(todo[j]):
                    print str(out) + " => " + str(todo[j]) + " : " + str(conf(supp(out), supp(todo[j]))) + "%"