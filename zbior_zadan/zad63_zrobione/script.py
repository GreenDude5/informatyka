file1 = open("./63/ciagi.txt", "r")

def p1(file):
    for i in range(1000):
        sequence = [*str(file.readline().strip())]  
        doubleCycled = True
        leng = len(sequence)
        if leng % 2 != 0: doubleCycled = False; continue
        for j in range(int(leng/2)):
            if sequence[j] != sequence[int(leng/2)+j]: doubleCycled = False; continue
        if doubleCycled: print("".join(sequence))

def p2(file):
    count = 0   
    for i in range(1000):
        sequence = [*str(file.readline().strip())]
        qualified = True
        for j in range(1, len(sequence)):
            if int(sequence[j]) == 1 and int(sequence[j-1]) == 1: qualified = False
        if qualified: count += 1
    print(count)

def p3(file):
    count = 0
    minN = 999999
    maxN = -999999
    for i in range(1000):
        num = int(file.readline().strip(), 2)
        tmpN = num
        divs = []
        x = 2
        while num / 2 + 1 and num > 1:
            if num % x == 0:
                num //= x
                divs.append(x)
                continue
            x += 1
        if len(divs) == 2: 
            count += 1
            if tmpN > maxN: maxN = tmpN
            if tmpN < minN: minN = tmpN
        
    print(count, minN, maxN)
                


# p1(file1)
# p2(file1)
p3(file1)