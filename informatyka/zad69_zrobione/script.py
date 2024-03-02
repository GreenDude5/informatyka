file1 = open("./69/dane_geny.txt", "r")

def p1(file):
    species = {}
    for i in range(1000):
        row = file.readline().strip()
        l = len(row)
        if l in species: species[l] += 1
        else: species[l] = 1
    
    maxNum = list(species.keys())[0]
    for n in species:
        if species[n] > species[maxNum]: maxNum = n
    
    print(len(species))
    print(species[maxNum])    

def p2(file):
    count = 0
    genes = []
    for i in range(1000):
        row = file.readline().strip()
        current = ""
        for j in range(1, len(row)):
            if row[j-1:j+1] == "AA":
                if current == "": current = "AA"; continue
            if row[j-1:j+1] == "BB":
                if current != "": 
                    current += "B"
                    genes.append(current)
                    current = ""
                    continue
            if current != "": current += row[j]; 
    for g in genes:
        if "BCDDC" in g: count += 1
    print(count)

def p3(file):
    maxLen = 0
    maxGen = 0
    for i in range(1000):
        row = file.readline().strip()
        countGen = 0
        current = ""
        for j in range(1, len(row)):
            if row[j-1:j+1] == "AA":
                if current == "": current = "AA"; continue
            if row[j-1:j+1] == "BB":
                if current != "":
                    current += "B"
                    countGen += 1
                    if len(current) > maxLen: maxLen = len(current)
                    current = ""
                    continue
            if current != "": current += row[j]
        if countGen > maxGen: maxGen = countGen
    print(maxGen)
    print(maxLen)

def p4(file):
    strong = 0
    resistant = 0
    for i in range(1000):
        row = file.readline().strip()
        revRow = row[::-1]
        if row == revRow: strong += 1; continue
        genes1 = ""; genes2 = ""
        current = ""
        for j in range(1, len(row)):
            if row[j-1:j+1] == "AA": current = "AA"; continue
            if row[j-1:j+1] == "BB":
                if current != "":
                    current += "B"
                    genes1 += current
                    current = ""
                    continue
            if current != "": current += row[j]

        current = ""
        for k in range(1, len(revRow)):
            if revRow[k-1:k+1] == "AA": current = "AA"; continue
            if revRow[k-1:k+1] == "BB":
                if current != "":
                    current += "B"
                    genes2 += current
                    current = ""
                    continue
            if current != "": current += revRow[k]
        
        if genes1 == genes2: resistant += 1
    
    print(resistant)
    print(strong)


# p1(file1)
# p2(file1)
# p3(file1)
p4(file1)