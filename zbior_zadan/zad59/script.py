file1 = open("./59/liczby.txt", "r")

def p1(file1):
    count = 0

    for lines in file1:
        valid = False
        tmp = 0
        elem = 3
        num = int(lines.strip())
        if num % 2 == 0: continue
        while num > 1:
            if (num % elem == 0): tmp += 1
            while num % elem == 0:
                num /= elem
            elem += 2
            if tmp > 3: break
        if tmp == 3: count += 1

    print(count)

def p2(file1):
    counter = 0
    for i in range(1000):
        num1 = file1.readline().strip()
        num2 = num1[::-1]
        sum1 = str(int(num1) + int(num2))
        if sum1 == sum1[::-1]: counter += 1
        
    print(counter)
        
def w(n):
    tmp = 1
    for i in n:
        tmp *= i
    return tmp
        
def p3(file1):
    arr = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1000):
        k = 0
        num = file1.readline().strip()
        while len(num) > 1:
            num = w(num)
            k += 1
        arr[k-1] += 1
        
    print(arr)

p1(file1)
# p2(file1)
# p3(file1)