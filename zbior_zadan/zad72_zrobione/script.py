file1 = open("./72/napisy.txt", "r")

def p1(file):
    count = 0
    idk = []
    for row in file:
        str1 = row.split(" ")[0]; str2 = row.split(" ")[1]
        if len(str1)*3 <= len(str2) or len(str2)*3 <= len(str1):
            count += 1
            idk.append(row)
    print(count)
    print(idk[0])

def p2(file):
    for row in file:
        str1 = row.split(" ")[0]; str2 = row.split(" ")[1]
        if str1 in str2[:len(str1)]:
            print(row, str2[len(str1):])

def p3(file):
    sim = []
    maxCount = 0
    for row in file:
        tmp = row.strip().split(" ")
        str1 = tmp[0]; str2 = tmp[1]
        leng = len(str1) if len(str1) < len(str2) else len(str2)
        count = 0
        for i in range(1, leng+1):
            if str1[-i] == str2[-i]: count += 1
            else: break
        if count > 0:
            if count > maxCount: maxCount = count
            sim.append([str1, str2, count])

    print(maxCount)
    for x in sim:
        if x[2] == maxCount: print(x[0], x[1])

        

        

# p1(file1)
# p2(file1)
p3(file1)