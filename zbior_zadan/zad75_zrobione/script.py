file1 = open("./75/tekst.txt", "r")
file2 = open("./75/probka.txt", "r")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(word, A, B):
    current = ''
    for c in word:
        num = letters.index(c)*A+B
        if num > 25: num = num % 26
        current += letters[num]
    return current

def p1(file):
    words = file.readline().strip().split(" ")
    for word in words:
        if word[0] == word[-1] == 'd': print(word)

def p2(file):
    words = file.readline().strip().split(" ")
    for word in words:
        if len(word) >= 10: print(cipher(word, 5, 2))

def p3(file):
    idx = 0
    for row in file:
        idx += 1
        words = row.strip().split(" ")
        cipherKey = []
        decipherKey = []
        for i in range(25 + 1):
            for j in range(25 + 1):
                if cipher(words[0], i, j) == words[1]: cipherKey = [i, j]
                if cipher(words[1], i, j) == words[0]: decipherKey = [i, j]
        print(f"{idx}: {cipherKey}, {decipherKey}")

# p1(file1)
# p2(file1)
p3(file2)