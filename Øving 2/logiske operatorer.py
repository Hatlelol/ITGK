#a) 1, 3, 5
#b)

print("Gi inn a og b, begge heltall i intervall <40,50> eller <70,90>:")
a = int(input("Verdi for a: "))
b = int(input("Verdi for b: "))

if ((90 > a > 70) or (50 > a > 40)) and ((70 < b < 90) or (50 > b > 40)):
    print("Tallene er begge i gyldige intervall ^u^")
else:
    print("Minst ett av tallene er utenfor et gyldig intervall :(")


#c)
print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))
s = input("Liker du pannekaker? J/N")

if s == "J":
    elskerpannekaker = True
else:
    elskerpannekaker = False

if (10 < p or p <= 0) or not elskerpannekaker:  # Kode mangler her
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10 - p
    print("Da blir det", p, "på deg og", r, "på meg :D")