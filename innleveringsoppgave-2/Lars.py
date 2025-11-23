
# Variabel som teller antall poeng
# Valg 1 gir 1 poeng, og valg 2 gir 2 poeng.
Sum_Poeng = 0

print("Del 2 Kode ting")
print("")
print("OBS! Case sensitive, Bruk store bokstaver")

# spørsmål 1
print("Spørsmål 1")
print("A: Valg 1")
print("B: Valg 2")
#Tom linje for å få litt plass mellom valgene, enklere å lese
print("")
# Input field for å svare, er samme for alle spørsmålene, må vel ikke kopiere det til alle?
valg1 = input("Velg A eller B: ")

# Hvis brukeren skriver A, gir den 1 poeng, alt annet gir 2 poeng, og antar at de velger B.
# ^^ Dette gjelder alle spørsmålene
if valg1 == "A":
    Sum_Poeng += 1
else:
    Sum_Poeng += 2

# spørsmål 2
print("Spørsmål 2")
print("A: Valg 1")
print("B: Valg 2")
print("")
valg2 = input("Velg A eller B: ")

if valg2 == "A":
    Sum_Poeng += 1
else:
    Sum_Poeng += 2

# spørsmål 3
print("Spørsmål 3")
print("A: Valg 1")
print("B: Valg 2")
print("")
valg3 = input("Velg A eller B: ")

if valg3 == "A":
    Sum_Poeng += 1
else:
    Sum_Poeng += 2

# Resultat
print("Resultat")
print("")

# litt logikk, hvis man bare velger A, får man totalt 3 poeng og ender opp med resultat 1.
# Velger man en blanding, får man mellom 4-5 poeng, og får 2.
# Velger man bare B, får man 6 poeng, og får det tredje resultatet. 
# Koden spesifiserer ikke 6 poeng på det siste alternativet, fordi det ikke er mulig å få mer en 6 :p
if Sum_Poeng <= 3:
    print("Resultat 1: tekst tekst tekst")
elif Sum_Poeng <= 5:
    print("Resultat 2: tekst tekst tekst")
else:
    print("Resultat 3: tekst tekst tekst")