
strcolnames = ""

def getfilecontents(filename):
    global strcolnames
    firstline = True
    filein = open(filename, 'r')
    lines = []
    line = filein.readline();
    while (line != ''):
        if firstline:
            strcolnames = line.strip('\n')
            firstline = False
        else:
            lines.append(line.strip('\n'))
        line = filein.readline()
    return lines




alumni = set(getfilecontents('pipedelimitedinputfile.txt'))
alumniJSON = '{"alumni":['
print(strcolnames)
strcolnames = strcolnames.replace(" ","")
col_names = strcolnames.split("|")
print (col_names)
f = open("alumniJSON.txt", "w")
f.write(alumniJSON)

alumnuscount = 0
for alumnus in sorted(alumni):
    #print(student)
    f.write('{ ')
    data = alumnus.split("|")
    for colnum in range(0,len(data)):
        f.write('"' + col_names[colnum] + '":"' + data[colnum] + '"')
        if colnum < len(data)-1:
            f.write(' , ')
    f.write(' }')
    if alumnuscount < len(alumni)-1:
        f.write(' , ')
    alumnuscount += 1

f.write(' ]}')

f.close()
print ("Completed")
