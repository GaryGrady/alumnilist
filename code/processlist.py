import re


def getfilecontents(filename,stripnewlinebool):
    filein = open(filename, 'r')
    lines = []
    line = filein.readline();
    while (line != ''):
         #print(line)
         if stripnewlinebool:
             lines.append(line.strip('\n'))
         else:
            lines.append(line)
         line = filein.readline()
    return lines

students = set(getfilecontents('filenames.txt',True))

studentslist = []
for student in sorted(students):
    print(student)
    data = student[:-4].split("_")
    number = int(data[0])
    names = re.sub( r"([A-Z])", r" \1", data[1]).split()
    studentdata = [number,names,student]
    studentslist.append(studentdata)

#print studentset
countof2name = 0
countof3name = 0
countofall = 0
for student in studentslist:
    if len(student[1]) == 2:
        countof2name += 1
    elif len(student[1]) == 3:
        if student[1][1] in ["De","La","Mc","O"]:
            student[1][1] = student[1][1] + student[1][2]
            del student[1][2]
        elif student[1][2] == "Jr":
            student[1][1] = student[1][1] + " " + student[1][2]
            del student[1][2]
        else:
            student[1][0] = student[1][0] + " " + student[1][1]
            student[1][1] = student[1][2]
            del student[1][2]
        countof2name += 1

    countofall += 1
html = "<html><head></head><body>"
css = "".join(getfilecontents('layout.css',False))
grid = '<div class="wrapper">'

gridstudents = ""

for student in studentslist:
    gridstudent = '<div class = "student" id=#studimgdata# onclick="showdata(#studimgdata#)"><img src="#studimg#" alt="#studname#" />'
    gridstudent = gridstudent.replace("#studimgdata#", "'" + student[2][0:len(student[2])-4] + "'")
    gridstudent = gridstudent.replace("#studimg#", student[2])
    gridstudent = gridstudent.replace("#studname#", student[1][0] + " " + student[1][1])
    gridstudents += gridstudent + "</div>"


gridend = "</div>"
htmlend = "</body><html>"
fileout =  open('layout.html', 'w')
fileout.write(html + '\n' + css + '\n' + grid  + '\n' +gridstudents + gridend + htmlend )
fileout.close()
print (countof2name)
print (countof3name)
print (countofall)
#print(sorted(students))
