file1 = open('./94/wzrost.txt')

def p1(file):
    lines = file.readlines()
    maxInc = 0; maxId = 0
    for i in range(1, len(lines)):
        line = lines[i].strip().split(";")
        inc = int(line[-1]) / int(line[2]) * 100
        if inc > maxInc: maxInc = inc; maxId = line[0]
    print(f"{maxId}: {maxInc}")

def p2(file):
    lines = file.readlines()
    boys = []; girls = []
    for i in range(1, len(lines)):
        line = lines[i].strip().split(";")
        if line[1] == 'd': girls.append(line)
        else: boys.append(line)
    
    for j in range(19):
        avgBoy = 0; avgGirl = 0
        tmpb = 0; tmpg = 0
        for boy in boys:
            tmpb += int(boy[2+j])
        for girl in girls:
            tmpg += int(girl[2+j])
        avgBoy = tmpb / len(boys)
        avgGirl = tmpg / len(girls)
        if int(avgGirl) > int(avgBoy) + 1: print(j)
            
def p3(file):
    count = 0
    lines = file.readlines()
    for i in range(1, len(lines)):
        line = lines[i].strip().split(";")
        if line [2 + 15] == line[-1]: count += 1
    print(count)

def p4(file):
    lines = file.readlines()
    for i in range(1, len(lines)):
        line = lines[i].strip().split(";")
        # nie chce mi się tego robić



# p1(file1)
# p2(file1)
# p3(file1)
p4(file1)