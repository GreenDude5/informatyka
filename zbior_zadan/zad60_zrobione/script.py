file1 = open("./60/liczby.txt", "r")

def p1(file1):
    counter = 0
    arr = []
    for i in range(200):
        num = int(file1.readline().strip())
        if num < 1000: counter += 1; arr.append(num)
        
    print(counter)
    print(arr[-1], arr[-2])

def p2(file1):
    for i in range(200):
        num = int(file1.readline().strip())
        divs = 0
        for j in range(1, num+1):
            if num % j == 0: divs += 1
        if divs == 18: 
            print(num)
            for k in range(1, num+1):
                if num % k == 0: print(k, end=" ")
            print("")

def p3(file1):
    def nwd(x, y):
        if x < y: return nwd(y, x)
        if y == 0: return x
        return nwd(y, x%y)
    
    arr = []

    for nums in file1:
        arr.append(int(nums.strip()))

    maxNum = 0
    for i in range(200):
        ok = True
        for j in range(200):
            if i != j and nwd(arr[i], arr[j]) > 1:
                ok = False
        if ok and arr[i] > maxNum:
            maxNum = arr[i]
    
    print(maxNum)

# p1(file1)
# p2(file1)
p3(file1)