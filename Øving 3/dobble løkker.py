i = 5
for x in range(i):
    for y in range(x+1):
        print(y+1, end=" ")
    print()
for x in range(i):
    print("#", end="")
    for y in range(x+1):
        print(" ", end="")
    print("#")


tall = int(input("Skriv inn et positivt heltall"))
arr = []

if tall == 1 or tall == 2 or tall == 3:
    print(tall, "er et primtall")
else:
    x = 100
    for i in range(2, x):
          while tall%i == 0:
              tall = tall/i
              arr.append(i)

print(arr)