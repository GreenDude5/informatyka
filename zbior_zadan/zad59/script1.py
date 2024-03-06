numbers = open("./59/liczby.txt","r")


#def zad1():
#    count = 0
#    
#    for line in numbers:
#        divs = []
#        i = 2
#        while True:
#            if 
#            if line % i == 0:
#                diva.append(i)
#                line /= i
#            i+=1


def zad2():
    count = 0
    
    for line in numbers:
        num1 = int(line)
        num2 = int(str(num1)[::-1])
        summ = num1 + num2
        if str(summ)[::-1] == str(summ):
            count += 1
            
    print(count)
    
def zad3():
    
    
#zad2()
        