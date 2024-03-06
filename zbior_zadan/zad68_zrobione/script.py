file1 = open("./68/dane_napisy.txt", "r")

def p1(file):
    count = 0
    for i in range(1000):
        txt = file.readline().strip().split(" ")
        if txt[0].count(txt[0][0]) == len(txt[0]) and txt[0] == txt[1]: count += 1
    print(count)

def p2(file):
    count = 0
    for i in range(1000):
        txt = file.readline().strip().split(" ")
        str1 = [*txt[0]]; str2 = [*txt[1]]
        str1.sort(); str2.sort()
        if str1 == str2: count += 1
    print(count)

def p3(file):
    rows = []
    for i in range(1000):
        txt = file.readline().strip().split(" ")
        rows.append(txt[0])
        rows.append(txt[1])
    
    maxCount = 0
    for x in range(len(rows)):
        str1 = [*rows[x]]
        str1.sort()
        count = 1
        for y in range(len(rows)):
            if y == x: continue
            str2 = [*rows[y]]
            str2.sort()
            if str1 == str2: count += 1
        if count > maxCount: maxCount = count
    print(maxCount)

# p1(file1)
# p2(file1)
# p3(file1)