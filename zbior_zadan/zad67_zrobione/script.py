def fib(n):
    if n == 1 or n == 2: return 1
    else:
        return fib(n-1) + fib(n-2)
    
def p1():
    print(fib(10))
    print(fib(20))
    print(fib(30))
    print(fib(40))

def p2():
    for i in range(1, 40 + 1):
        num = fib(i)
        isPrime = False
        for j in range(2, int(num / 2) + 1):
            if num % j == 0: isPrime = True; break
        if isPrime: print(num)

def p3():
    for i in range(1, 40 + 1):
        num = fib(i)
        numBin = str(bin(num)).removeprefix('0b')
        print(numBin)

    # powinienem jeszcze tu pobawić się w zobrazowanie tego fraktala, ale nie chce mi się
        
def p4():
    for i in range(1, 40 + 1):
        num = fib(i)
        numBin = str(bin(num)).removeprefix('0b')
        if numBin.count('1') == 6: print(numBin)

# p1()
# p2()
# p3()
# p4()
