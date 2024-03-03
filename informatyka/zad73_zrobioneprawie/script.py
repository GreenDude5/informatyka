with open("./73/tekst.txt") as f:
    words = [x for x in f.readline().strip().split(" ")]
vowels = "AEIOUY"

def p1(words):
    count = 0
    for word in words:
        if len(word) == 1: continue
        for i in range(1, len(word)):
            if word[i] == word[i-1]: count += 1

    print(count)

def p2(words):
    letters = {}
    for word in words:
        for char in word:
            if char not in letters: letters[char] = 1
            else: letters[char] += 1
    
    countMax = sum(letters.values())
    sortedLetters = dict(sorted(letters.items()))
    for letter in sortedLetters:
        print(f"{letter}: {sortedLetters[letter]} ({round(sortedLetters[letter]/countMax*100, 2)}%)")
        
def p3(words):
    maxCount = 0
    data = []
    longestOrSmth = []
    for word in words:
        count = 0
        current = ""
        for i in range(len(word)):
            if word[i] not in vowels:
                if current == "": current += word[i]; count += 1; continue
                else: current += word[i]; count += 1
            else:
                if current == "": continue
                else: data.append([word, current, count]); current = ""; maxCount = count if count > maxCount else maxCount

    anotherCount = 0
    for ele in data:
        if ele[2] == maxCount:
            anotherCount += 1
            longestOrSmth.append(ele[0])

    print(maxCount)
    print(len(longestOrSmth))
    print(longestOrSmth[0])
            

# p1(words)
# p2(words)
# p3(words)