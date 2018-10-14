numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
threshold = 5
mindre = []
stor = []

for i in numbers:
    if i < threshold:
        mindre.append(i)
    else:
        stor.append(i)

print(mindre, stor)

def gangetabell(n):
    matrise = []
    for i in range(1, n):
        arr = []
        for x in range(1, n):
            arr.append(i*x)
        matrise.append(arr)
    print(matrise)


gangetabell(int(input("Skriv et heltall"))+1)
