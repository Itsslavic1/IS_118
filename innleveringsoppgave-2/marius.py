print("Hei! Du er Erling, prosjektleder for et lite team.")
print()
print("Teamet har hatt det litt tøft, og du må ta noen viktige valg.")
print()
# team_score er en variabel som jeg bruker for å holde styr på hvordan det går i teamet. Jeg fikk inspirasjon for dette systemet fra gruppen.
# Når Erling tar gode valg -> pluss poeng.
# Når Erling tar dårlige valg ->  minus poeng.

team_score = 0

# ---------------- VALG 1 ----------------
print("1) Silje og Sivert")
print("De har gått fra en saklig uenighet til en mer personlig konflikt.")
print()

print("A: Ha en rolig samtale der begge får forklare seg.")
print("B: Ha en rask avstemning for å bestemme løsningen.")

# Jeg lagrer svaret bruker skriver inn i variabelen svar1
svar1 = input("Velg A eller B: ").upper()

# .upper() gjør svaret om til stor bokstav,
# slik at både "a" og "A" blir det samme.
# If-sjekk: hvis brukeren valgte A

if svar1 == "A":
    print()
    print("Du har et møte med dem. De får snakket sammen, og det hjelper litt.")
    team_score += 1
else:
    print()
    print("Du tar en avstemning. Det går raskt, men Silje føler seg overkjørt.")
    team_score -= 1


# ---------------- VALG 2 ----------------
print("2) Hamdi og Jabir")
print("De er uenige om hvordan digitale folkemøter skal fungere.")
print()

print("A: Gi dem en liten oppgave de må løse sammen.")
print("B: Ha en lengre prat for å finne en løsning begge liker.")

svar2 = input("Velg A eller B: ").upper()

if svar2 == "A":
    print()
    print("De jobber sammen på minioppgaven og samarbeidet blir bedre.")
    team_score += 1
else:
    print()
    print("Dere snakker ordentlig gjennom uenigheten, og de finner en løsning.")
    team_score += 1


# ---------------- VALG 3 ----------------
print("3) Motivasjonen i teamet")
print("Teamet virker slitent og umotivert.")
print()

print("A: Ta en liten sosial pause.")
print("B: Lage en tydelig plan med delmål.")

svar3 = input("Velg A eller B: ").upper()

if svar3 == "A":
    print()
    print("Pausen gjør stemningen litt bedre.")
    team_score += 1
else:
    print()
    print("Planen gir struktur, men noen blir mer stresset.")
    team_score -= 1

# ---------------- SLUTTEN ----------------
print("RESULTAT:")
print()

# Nå bruker jeg team_score for å bestemme hvilken avslutning man får.
# Dette er sluttpoenget for hele spillet.

if team_score >= 2:
    # Hvis man har 2 eller 3 poeng → god slutt
    print("SLUTT 1: Teamet samarbeider bra og leverer prototypen i tide.")
    print("Konfliktene er ikke helt borte, men dere er på vei inn i norming-fasen.")
elif team_score <= -1:
    # Hvis man har -1, -2 eller -3 → dårlig slutt
    print("SLUTT 3: Prosjektet sliter. Teamet mister motivasjon og blir forsinket.")
else:
     # Hvis man har 0 eller 1 poeng → middels slutt
    print("SLUTT 2: Dere leverer prototypen, men stemningen er fortsatt litt sår.")

print()
print("Slutt på Marius sitt forslag.")