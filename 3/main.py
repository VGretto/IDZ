buffer = []

file_name = raw_input('file:')
file = open(file_name, "r")

for line in file:
    buffer.append(line)

for i in range(0, buffer.__len__(), 1):
    buffer[i] = buffer[i].split(',')

for i in range(0, buffer.__len__(), 1):
    buffer[i][4] = buffer[i][4].split('\n')[0]

print('\nDataBase:')
for i in range(0, buffer.__len__(), 1):
        print buffer[i]

file.close()

while 1:
    print('\n===CMD===\n1.Print\n2.Element edit\n3.Compare\n--------------\ns.Save')
    ans = raw_input('answer:')
    if ans == '1':
        print('\nDataBase:')
        for i in range(0, buffer.__len__(), 1):
            print buffer[i]
    elif ans == '2':
        tmp = raw_input('In with line?:')
        print buffer[int(tmp)-1]
        l = int(tmp)-1
        tmp = raw_input('In with column?:')
        buffer[l][int(tmp)-1] = raw_input(buffer[l][int(tmp)-1]+':')
    elif ans == '3':
        tmp = raw_input('First line:')
        fl = int(tmp)-1
        tmp = raw_input('Second line:')
        sl = int(tmp)-1
        for i in range(0,buffer[0].__len__()):
            print('{0} <-> {1}'.format(buffer[fl][i], buffer[sl][i]))
    elif ans == 's':
        file = open(file_name, "w")
        for i in range(0,buffer.__len__(), 1):
            for j in range(0, buffer[i].__len__(), 1):
                file.write(buffer[i][j])
                if j+1 < buffer[i].__len__():
                    file.write(',')
            file.write('\n')

        file.close()
