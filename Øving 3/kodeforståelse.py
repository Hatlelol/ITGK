a=345
b=''
while a or b=='':
    b=str(a%2)+b
    a=a//2
print(b) #printer ut restene etter å dividere a med 2 til a = 0

for x in range(0, 10, 2):
    print(x, end='')
    if x%4==0:
        print( ": Dette tallet går opp i 4-gangern")
    else:
        print()#printer ut partall fra null til 10 og markerer de som går opp i 4 gangen

i = 1
while i<10:
    i = i*2
print(i) #printer den første 2er potensen som er over 10 dvs 16

i = 1
j = 3
while j>0:
    i = i*2
    j = j - 1
print(i) #skriver ut den 3. 2er potensen, dvs 8

i = 5
for x in range(i):
    for y in range(x+1):
        print("*", end="")
    print() #lager en "trapp" med * nedover, dvs første rad har en * neste har to osv til det er 5 rader der den siste har 6 *