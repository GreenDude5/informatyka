a = 0.02
b = 0.0005
c = 0.05

Z = 100
W = 30

def p1():   
    Z = 100; W = 30
    for i in range(1, 5*12):
        nZ = round(Z + a*Z - b*Z*W, 2)
        nW = round(W + b*Z*W - c*W, 2)
        Z = nZ
        W = nW

    print(Z, W)

def p2():
    Z = 100; W = 30
    odpZ = 0; odpW = 0
    k = 1
    while odpZ == 0 and odpW == 0:
        nZ = round(Z + a*Z - b*Z*W, 2)
        nW = round(W + b*Z*W - c*W, 2)
        if nZ < Z and odpZ == 0: odpZ = k
        if nW < W and odpW == 0: odpW = k
        Z = nZ
        W = nW
        k += 1
    
    print(odpZ, odpW)
    
def p3():
    Z = 100; W = 30
    print(f"0 {Z} {W}")
    for i in range(1, 20*12):
        nZ = round(Z + a*Z - b*Z*W, 2)
        nW = round(W + b*Z*W - c*W, 2)
        Z = nZ
        W = nW
        print(f"{i} {Z} {W}")

# p1()
# p2()
p3()