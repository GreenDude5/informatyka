file1 = open("./61/ciagi.txt", "r")
file2 = open("./61/bledne.txt", "r")

def p1(file):
    count = 0; maxDiff = 0
    for i in range(100):
        length = file.readline().strip()
        sequence = file.readline().strip().split(" ")
        diff = int(sequence[1]) - int(sequence[0])
        isAritmetic = True
        for j in range(1, len(sequence)):
            if int(sequence[j]) - int(sequence[j-1]) != diff:
                isAritmetic = False
        if isAritmetic:
            count += 1
            if diff > maxDiff: maxDiff = diff
    print(count)
    print(maxDiff)

def p2(file):
    for i in range(100):
        length = file.readline().strip()
        sequence = file.readline().strip().split(" ")
        maxNum = 0
        isCube = False
        for j in range(len(sequence)):
            root = round(int(sequence[j])**(1/3), 6)
            if root == int(root): 
                isCube = True
                if int(sequence[j]) > maxNum: maxNum = int(sequence[j])
        if isCube: print(maxNum)
        
def p3(file):
    pass

# p1(file1)
# p2(file1)
p3(file2)