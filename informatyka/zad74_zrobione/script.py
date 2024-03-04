file1 = open("./74/hasla.txt", "r")
numbers = "0123456789"
lettersBig = "ABCDEFGHIJKLMNOQPRSTUVWXYZ"
lettersSmall = "abcdefghijklmnoqprstuvwxyz"

def p1(file):
    count = 0
    for password in file:
        password = password.strip()
        onlyNums = True
        for char in password:
            if char not in numbers: onlyNums = False; break
        if onlyNums: count += 1
    print(count)

def p2(file):
    passwords = {}
    for password in file:
        password = password.strip()
        if password not in passwords: passwords[password] = 1
        else: passwords[password] += 1
    
    sortedPass = []
    for passw in passwords:
        if passwords[passw] >= 2: sortedPass.append(passw)
    
    sortedPass.sort()
    for x in sortedPass: print(x)

def p3(file):
    count = 0
    for password in file:
        password = password.strip()
        if len(password) < 4: continue
        isAscii = True
        for i in range(len(password) - 4 + 1):
            frag = password[i:i+4]
            f = "".join(sorted(list(frag)))
            for c in range(len(f) - 1):
                if ord(f[c + 1]) - ord(f[c]) != 1: isAscii = False; break
        if isAscii: count += 1
    print(count)

def p4(file):
    count = 0
    for password in file:
        password = password.strip()
        hasNum = False; hasBigLetter = False; hasSmallLetter = False
        for char in password:
            if char in numbers: hasNum = True; continue
            if char in lettersBig: hasBigLetter = True; continue
            if char in lettersSmall: hasSmallLetter = True; continue
        if hasNum and hasBigLetter and hasSmallLetter: count += 1
    print(count)


# p1(file1)
# p2(file1)
# p3(file1)
p4(file1)