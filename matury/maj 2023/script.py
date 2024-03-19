arr = []

def shelf():
    for i in range(4):
        arr.append([])
        for j in range(2**i):
            arr[i].append([])

shelf()

numbers = [10, 2, 15, 13, 1, 5, 25]

for num in numbers:
    for i in range(len(arr)):
        for j in range(2**i):
            if arr[i][j] == []: arr[i][j] = num
            else:
                if num < arr[i][j]: arr[i+1][2*j-1]