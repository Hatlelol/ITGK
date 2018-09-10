h = float(input("Skriv inn høyden på tetraederet"))
a = 3*h/(6**0.5)
AT = (3**0.5)*(a**2)
V = ((2**0.5)*a**3)/12

print("Et tetraeder med h = ", h, " har et areal = ", round(AT, 3), "og et volum = ", round(V, 3))

