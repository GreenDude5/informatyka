file1 = open("./62/liczby1.txt", "r")
file2 = open("./62/liczby2.txt", "r")

def p1(file):
    maxNum = -999999; minNum = 999999
    for i in range(1000):
        num = int(file.readline().strip(), 8)
        if num > maxNum: maxNum = num
        if num < minNum: minNum = num

    maxNum = oct(maxNum)
    minNum = oct(minNum)
    print(minNum, maxNum)

def p2(file):
    numbers = []
    for i in range(1000):
        num = int(file.readline().strip())
        numbers.append(num)

    sequence = []
    tmpseq = []
    for j in range(1, 1000):
        if numbers[j] >= numbers[j-1]: tmpseq.append(numbers[j])
        else: 
            if len(tmpseq) > len(sequence): sequence = tmpseq
            tmpseq = []
    print(sequence)

def p3(file1, file2):
    countEq = 0; countHi = 0
    for i in range(1000):
        num1 = int(file1.readline().strip(), 8)
        num2 = int(file2.readline().strip(), 10)
        if num1 == num2: countEq += 1
        if num1 > num2: countHi += 1

    print(countEq, countHi)

def p4(file):
    countDec = 0; countOct = 0
    for i in range(1000):
        numDec = int(file.readline().strip())
        numOct = int(str(oct(numDec)).removeprefix("0o"))
        for j in [*str(numDec)]:
            if int(j) == 6: countDec += 1
        for k in [*str(numOct)]:
            if int(k) == 6: countOct += 1

    print(countDec)
    print(countOct)

# p1(file1)
# p2(file2)
# p3(file1, file2)
p4(file2)