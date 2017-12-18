input = open("input.csv", "r")
output = open("output.txt", "w")

buffer = []

for line in input:
    buffer.append(line)

for i in range(0, buffer.__len__(), 1):
    buffer[i] = buffer[i].split(',')

tmp = raw_input('Change anything? (y/n):')
if tmp == 'y':
    for i in range(0, buffer.__len__(), 1):
        print buffer[i]

    tmp = raw_input('In with line?:')
    print buffer[int(tmp)]
    l = int(tmp)
    tmp = raw_input('In with column?:')
    print buffer[l][int(tmp)]
    c = int(tmp)
    tmp = raw_input('In with letter start?:')
    e = int(tmp)
    txt = raw_input('type:')
    buffer[l][c] = buffer[l][c][:e] + txt + buffer[l][c][e:]

for item in buffer:
  print>>output, item
