file1 = open("./76/szyfr1.txt","r")
file2 = open("./76/szyfr2.txt","r")
file3 = open("./76/szyfr3.txt","r")

def cipher(word, key):
    current = [*word.strip()]
    n = len(key)
    for i in range(len(word)-1):
        current[i], current[int(key[i%n]) - 1] = current[int(key[i%n]) - 1], current[i]
    return "".join(current)

def decipher(word, key):
    current = [*word.strip()]
    n = len(key)
    for i in range(len(word)-1, -1, -1):
        current[i], current[int(key[i%n]) - 1] = current[int(key[i%n]) - 1], current[i]
    return "".join(current)

def p1(file):
    rows = file.readlines()
    words = rows[:-1]; key = rows[-1].split(" ")
    for word in words:
        print(cipher(word, key))

def p2(file):
    rows = file.readlines()
    word = rows[0].strip(); key = rows[-1].split(" ")
    print(cipher(word, key))

def p3(file):
    word = file.readline().strip()
    key = [6, 2, 4, 1, 5, 3]
    print(decipher(word, key))

# p1(file1)
# p2(file2)
# p3(file3)