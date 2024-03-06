file1 = open("./66/trojki.txt", "r")

def p1(file):
    for i in range(1000):
        nums = file.readline().strip().split(" ")
        num1 = int(nums[0]); num2 = int(nums[1]); num3 = int(nums[2])
        sumOfSmth = 0
        for x in str(num1): sumOfSmth += int(x)
        for y in str(num2): sumOfSmth += int(y)
        if sumOfSmth == num3: print(num1, num2, num3)

def p2(file):
    for i in range(1000):
        nums = file.readline().strip().split(" ")
        num1 = int(nums[0]); num2 = int(nums[1]); num3 = int(nums[2])
        isOdd1 = True; isOdd2 = True
        for x in range(2, int(num1 / 2) + 1):
            if num1 % x == 0: isOdd1 = False; break
        for y in range(2, int(num2 / 2) + 1):
            if num2 % y == 0: isOdd2 = False; break
        if isOdd1 and isOdd2 and num1 * num2 == num3: print(num1, num2, num3)

def p3(file):
    # first row
    nums = file.readline().strip().split(" ")
    num1 = int(nums[0]); num2 = int(nums[1]); num3 = int(nums[2])
    
    prevRow = [num1, num2, num3]
    if max(num1, num2, num3) == num3: isPitagorean = num1**2 + num2**2 == num3**2 # True / False 
    elif max(num1, num2, num3) == num2: isPitagorean = num1**2 + num3**2 == num2**2 # True / False 
    elif max(num1, num2, num3) == num1: isPitagorean = num3**2 + num2**2 == num1**2 # True / False 
    for i in range(1, 1000):
        nums = file.readline().strip().split(" ")
        num1 = int(nums[0]); num2 = int(nums[1]); num3 = int(nums[2])
        if max(num1, num2, num3) == num3: isPitagorean = num1**2 + num2**2 == num3**2 # True / False 
        elif max(num1, num2, num3) == num2: isPitagorean = num1**2 + num3**2 == num2**2 # True / False 
        elif max(num1, num2, num3) == num1: isPitagorean = num3**2 + num2**2 == num1**2 # True / False 
        if isPitagorean and prevPitagorean:
            print(prevRow[0], prevRow[1], prevRow[2])
            print(num1, num2, num3)

        prevRow = [num1, num2, num3]
        prevPitagorean = isPitagorean

def p4(file):
    count = 0
    maxLength = 0
    tmpLength = 0
    for i in range(1000):
        nums = file.readline().strip().split(" ")
        num1 = int(nums[0]); num2 = int(nums[1]); num3 = int(nums[2])
        isTriangle = num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1 # True / False
        if isTriangle: count += 1; tmpLength += 1
        else: tmpLength = 0
        if tmpLength > maxLength: maxLength = tmpLength

    print(count)
    print(maxLength)


# p1(file1)
# p2(file1)
# p3(file1)
# p4(file1)