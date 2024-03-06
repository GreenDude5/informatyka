import math

file1 = open("./65/dane_ulamki.txt", "r")

def p1(file):
    minFrag = 999999
    minFragNominator = 999999
    minFragDenominator = 999999
    for i in range(1000):
        frag = file.readline().strip().split(" ")
        nominator = int(frag[0]); denominator = int(frag[1])
        num = round(nominator / denominator, 6)
        if num < minFrag: minFrag = num; minFragNominator = nominator; minFragDenominator = denominator
        elif num == minFrag:
            if denominator < minFragDenominator: minFrag = num; minFragNominator = nominator; minFragDenominator = denominator

    print(minFragNominator, minFragDenominator)

def p2(file):
    count = 0
    for i in range(1000):
        frag = file.readline().strip().split(" ")
        nominator = int(frag[0]); denominator = int(frag[1])
        gcd = math.gcd(nominator, denominator)
        if gcd == 1: count += 1

    print(count)

def p3(file):
    sumOfNominators = 0
    for i in range(1000):
        frag = file.readline().strip().split(" ")
        nominator = int(frag[0]); denominator = int(frag[1])
        nominator = int(nominator / math.gcd(nominator, denominator))
        denominator = int(denominator / math.gcd(nominator, denominator))
        sumOfNominators += nominator

    print(sumOfNominators)

def p4(file):
    b = 2**2 * 3**2 * 5**2 * 7**2 * 13
    huh = 0
    for i in range(1000):
        frag = file.readline().strip().split(" ")
        nominator = int(frag[0])*b; denominator = int(frag[1])
        huh += (nominator / denominator)
    
    print(int(huh))




# p1(file1)
# p2(file1)
# p3(file1)
# p4(file1)