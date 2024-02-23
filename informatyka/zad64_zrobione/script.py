file1 = open("./64/dane_obrazki.txt", "r")

def p1(file):
    images = []
    current = []
    for row in file:
        if row.strip() == "": images.append(current); current = []
        else: current.append(row.strip())
    images.append(current) #last image

    reverse = 0; maxBlack = 0
    for img in images:
        black = 0; white = 0
        for row in img[:-1]:
            for pixel in row[:-1]:
                if pixel == "0": white += 1
                else: black += 1
        if black > white: reverse += 1
        if black > maxBlack: maxBlack = black

    print(reverse)
    print(maxBlack)

def p2(file):
    images = []
    current = []
    for row in file:
        if row.strip() == "": images.append(current); current = []
        else: current.append(row.strip())
    images.append(current) #last image 

    count = 0; first = []
    for img in images:
        isRecouring = True
        o1 = []; o2 = []; o3 = []; o4 = []
        for x in range(10):
            tmp = ""
            for y in range(10): tmp += img[x][y]
            o1.append(tmp)
        for x in range(10, 20):
            tmp = ""
            for y in range(10): tmp += img[x][y]
            o2.append(tmp)
        for x in range(10):
            tmp = ""
            for y in range(10, 20): tmp += img[x][y]
            o3.append(tmp)
        for x in range(10, 20):
            tmp = ""
            for y in range(10, 20): tmp += img[x][y]
            o4.append(tmp)
        
        c1 = True; c2 = True; c3 = True
        for x in range(len(o1)):
            for y in range(len(o2)):
                if o1[x][y] != o2[x][y]: c1 = False
        for x in range(len(o1)):
            for y in range(len(o3)):
                if o1[x][y] != o3[x][y]: c2 = False
        for x in range(len(o1)):
            for y in range(len(o4)):
                if o1[x][y] != o4[x][y]: c3 = False

        if not (c1 and c2 and c3): isRecouring = False
        if isRecouring:
            count += 1
            if len(first) == 0: first = img
    
    print(count)
    print("\n".join(first))

def p3(file):
    images = []
    current = []
    for row in file:
        if row.strip() == "": images.append(current); current = []
        else: current.append(row.strip())
    images.append(current) #last image

    correct = 0; fixable = 0; incorrect = 0; most = 0
    for img in images:
        incorrectRows = 0; incorrectCols = 0
        for row in img[:-1]:
            count = 0
            for pixel in row[:-1]:
                if pixel == "1": count += 1
            if count % 2 == 0: count = "0"
            else: count = "1"
            if count != row[-1]: incorrectRows += 1
        for col in range(len(img) - 1):
            count = 0
            for row in range(len(img) - 1):
                if img[row][col] == "1": count += 1
            if count % 2 == 0: count = "0"
            else: count = "1"
            if count != img[len(img) - 1][col]: incorrectCols += 1
        
        if incorrectRows == 0 and incorrectCols == 0: correct += 1
        elif incorrectRows <= 1 and incorrectCols <= 1: fixable += 1
        else: incorrect += 1

        if incorrectCols + incorrectRows > most: most = incorrectRows + incorrectCols

    print(correct)
    print(fixable)
    print(incorrect)
    print(most)

def p4(file):
    images = []
    current = []
    for row in file:
        if row.strip() == "": images.append(current); current = []
        else: current.append(row.strip())
    images.append(current) #last image

    n = 20
    idx = 0
    for img in images:
        idx += 1
        incorrectRows = 0; incorrectCols = 0
        for row in img[:-1]:
            count = 0
            for pixel in row[:-1]:
                if pixel == "1": count += 1
            if count % 2 == 0: count = "0"
            else: count = "1"
            if count != row[-1]: incorrectRows += 1
        for col in range(len(img) - 1):
            count = 0
            for row in range(len(img) - 1):
                if img[row][col] == "1": count += 1
            if count % 2 == 0: count = "0"
            else: count = "1"
            if count != img[len(img) - 1][col]: incorrectCols += 1

        if incorrectRows == 0 and incorrectCols == 0: continue
        
        if incorrectRows <= 1 and incorrectCols <= 1:
            rowNum = 0; colNum = 0
            tmp = 0
            for row in img[:-1]:
                tmp += 1
                count = 0
                for pixel in row[:-1]:
                    if pixel == "1": count += 1
                if count % 2 == 0: count = "0"
                else: count = "1"
                if count != row[-1]: rowNum = tmp
                # else: rowNum = -1
            tmp = 0
            for col in range(len(img) - 1):
                tmp += 1
                count = 0
                for row in range(len(img) - 1):
                    if img[row][col] == "1": count += 1
                if count % 2 == 0: count = "0"
                else: count = "1"
                if count != img[len(img) - 1][col]: colNum = tmp
                # else: colNum = -1
            if incorrectRows == incorrectCols: print(f"{idx} - {rowNum} {colNum}")
            elif rowNum > 0: print(f"{idx} - {rowNum} {n + 1}")
            else: print(f"{idx} - {n + 1} {colNum}")


# p1(file1)
# p2(file1)
# p3(file1)
# p4(file1)