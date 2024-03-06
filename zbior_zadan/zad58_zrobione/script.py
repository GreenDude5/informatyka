import math

s1 = open("./58/dane_systemy1.txt", "r")
s2 = open("./58/dane_systemy2.txt", "r")
s3 = open("./58/dane_systemy3.txt", "r")

def p1(file1, file2, file3):
    min1 = 999999
    min2 = 999999
    min3 = 999999
    
    for i in range(1095):
        data1 = int(file1.readline().split(" ")[1],2)
        data2 = int(file2.readline().split(" ")[1],4)
        data3 = int(file3.readline().split(" ")[1],8)
        
        if data1 < min1: min1 = data1
        if data2 < min2: min2 = data2
        if data3 < min3: min3 = data3
        
    print(f"s1: {min1}")
    print(f"s2: {min2}")
    print(f"s3: {min3}")

def p2(file1, file2, file3):
    counter = 0
    state = 12
    for i in range(1095):
        data1 = int(file1.readline().split(" ")[0],2)
        data2 = int(file2.readline().split(" ")[0],4)
        data3 = int(file3.readline().split(" ")[0],8)
        if data1 != state and data2 != state and data3 != state:
            counter += 1
        state += 24
        
    print(counter)
    
def p3(file1, file2, file3):
    counter = 0
    max1 = 0
    max2 = 0
    max3 = 0
    for i in range(1095):
        newRecord = False
        data1 = int(file1.readline().split(" ")[1],2)
        data2 = int(file2.readline().split(" ")[1],4)
        data3 = int(file3.readline().split(" ")[1],8)
        
        if data1 > max1: max1 = data1; newRecord = True
        if data2 > max2: max2 = data2; newRecord = True
        if data3 > max3: max3 = data3; newRecord = True
        if newRecord: counter += 1
        
    print(counter)
    
def p4(file1):
    data = []
    for lines in file1:
        data.append(int(lines.split(" ")[1],2))
    
    maxJump = -999999
    for i in range(1095):
        for j in range(i+1, 1095):
            data1 = data[i]
            data2 = data[j]
            r = pow(data1 - data2, 2)
            diff = abs(i - j)
            jump = math.ceil(r / diff)
            if jump > maxJump: maxJump = jump
            
    print(maxJump)
            
            
            
p1(s1, s2, s3)
p2(s1, s2, s3)
p3(s1, s2, s3)
p4(s1)