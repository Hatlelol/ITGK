tall = 2.25
des = 0

arr = list(str(tall))
hel = []

for x in arr:
    if x == ".":
        break
    hel.append(x)
hel = ''.join(hel)
print(tall - int(hel))

