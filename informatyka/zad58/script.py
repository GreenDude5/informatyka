s1 = open("./58/dane_systemy1.txt", "r")
s2 = open("./58/dane_systemy2.txt", "r")
s3 = open("./58/dane_systemy3.txt", "r")

def p1():
    mintemperatura = 999999
    for lines in s3:
        dane = lines.split(" ")
        temperatura = int(dane[1],8)
        if temperatura < mintemperatura:
            mintemperatura = temperatura
        print(" " + str(temperatura))
    print(mintemperatura)

def p2(file1, file2, file3):
    faulty1 = []
    lasttime1 = 0
    for lines in file1:
        dane = lines.split(" ")
        zegar = int(dane[0],2)
        if zegar != lasttime1 + 24:
            faulty1.append(zegar)
            
    faulty2 = []
    lasttime2 = 0
    for lines in file2:
        dane = lines.split(" ")
        zegar = int(dane[0],4)
        if zegar != lasttime2 + 24:
            faulty2.append(zegar)
            
    faulty3 = []
    lasttime3 = 0
    for lines in file3:
        dane = lines.split(" ")
        zegar = int(dane[0],8)
        if zegar != lasttime3 + 24:
            faulty3.append(zegar)
            
    faulty1.pop(0)
    faulty2.pop(0)
    faulty3.pop(0)
    
    matches = []
    
    for i in faulty1:
        if i in faulty2 and i in faulty3:
            matches.append(i)
    print(matches)
    print(len(matches))
    
def p3(file1, file2, file3):
    lastday1 = -999999
    records1 = []
    for lines in file1:
        dane = lines.split(" ")
        temperatura = int(dane[1],2)
        if temperatura > lastday1:
            records1.append(temperatura)
        lastday1 = temperatura
        
    lastday2 = -999999
    records2 = []
    for lines in file2:
        dane = lines.split(" ")
        temperatura = int(dane[1],4)
        if temperatura > lastday2:
            records2.append(temperatura)
        lastday2 = temperatura
        
    lastday3 = -999999
    records3 = []
    for lines in file3:
        dane = lines.split(" ")
        temperatura = int(dane[1],8)
        if temperatura > lastday3:
            records3.append(temperatura)
        lastday3 = temperatura

    recorddaycount = [len(records1), len(records2), len(records3)]
    print(min(recorddaycount))
    
p1()
#p2(s1, s2, s3)
#p3(s1, s2, s3)