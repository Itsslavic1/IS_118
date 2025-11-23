# Vetle.py – personlig versjon til IS-118 innleveringsoppgave 2
# Interaktiv historie der du spiller som Erling

def spør_bruker(tekst, alternativ_a, alternativ_b):
    """
    Viser et valg med a/b og sørger for at brukeren skriver gyldig input.
    """ 
    while True:
        print(tekst)
        print(f"a) {alternativ_a}")
        print(f"b) {alternativ_b}")
        svar = input("Velg a eller b: ").strip().lower()

        if svar == "a" or svar == "b":
            return svar
        else:
            print("Du må skrive a eller b. Prøv igjen.\n")


print("\n==============================")
print("  ERLING I STORMING-FASEN")
print("==============================\n")

print("Det er seks uker siden prosjektstart.")
print("To konflikter drar energi ut av teamet, og prototypen nærmer seg.\n")

# Skårer som påvirker sluttresultatet
samarbeid = 0   # hvor trygt/positivt teamet samarbeider
fremdrift = 0   # hvor bra dere ligger an mot prototypen

# -------------------- VALG 1 --------------------
valg1 = spør_bruker(
    "\nSituasjon 1:\nSilje og Sivert går i lås i et møte. Stemningen er merkbart skarp.\nHva velger Erling å gjøre her og nå?",
    "Stopper møtet og setter tydelige regler for diskusjon foran alle.",
    "Setter konflikten på pause og tar en-til-en prater senere."
)

if valg1 == "a":
    print("\nErling tar styring i rommet.")
    print("Det blir litt ubehagelig i øyeblikket, men rammene blir klare.")
    samarbeid += 1
    fremdrift -= 1
else:
    print("\nErling lar møtet gå videre og tar dem hver for seg etterpå.")
    print("Begge roer seg, men resten av teamet føler seg litt usikre.")
    samarbeid += 0
    fremdrift += 0


# -------------------- VALG 2 --------------------
valg2 = spør_bruker(
    "\nSituasjon 2:\nHamdi og Jabir sender passive-aggressive meldinger i chatten.\nDu ser at dette kan eksplodere senere.\nHva gjør Erling?",
    "Ber dem lage hvert sitt korte forslag først, så samler han dem i felles workshop.",
    "Lar dem jobbe videre som de vil, så lenge de leverer til fristen."
)

if valg2 == "a":
    print("\nErling strukturerer uenigheten.")
    print("Når de møtes igjen, har begge konkrete forslag, og de finner felles grunn.")
    samarbeid += 1
    fremdrift += 0
else:
    print("\nErling lar det gå.")
    print("De leverer hver sin løsning som krasjer, og irritasjonen øker.")
    samarbeid -= 1
    fremdrift -= 1


# -------------------- VALG 3 --------------------
valg3 = spør_bruker(
    "\nSituasjon 3:\nTeamet virker slitne og trekker seg tilbake i sine fagbobler.\nHvordan bygger Erling motivasjon nå?",
    "Setter av 30 min til å feire små seire og minne teamet på målet.",
    "Setter en hard plan og ber alle prioritere kun oppgavene."
)

if valg3 == "a":
    print("\nErling løfter blikket for teamet.")
    print("Folk smiler litt igjen, og det blir lettere å spørre om hjelp.")
    samarbeid += 1
    fremdrift += 0
else:
    print("\nErling legger press på leveranser.")
    print("Det gir fart, men flere blir stille og mindre åpne for samarbeid.")
    samarbeid -= 1
    fremdrift += 1


# -------------------- SLUTT --------------------
print("\n==============================")
print("           UTFALL")
print("==============================\n")

# Minst tre forskjellige sluttscenarier
if samarbeid >= 2 and fremdrift >= 0:
    print("Sterkt utfall:")
    print("Teamet samler seg, går inn i norming-fasen og prototypen blir solid.")
    print("Erling blir sett på som en trygg leder i en vanskelig fase.")
elif samarbeid >= 0:
    print("Blandet utfall:")
    print("Dere leverer en prototype, men samarbeidet er fortsatt skjørt.")
    print("Teamet trenger mer tid før de jobber helt sømløst.")
else:
    print("Svakt utfall:")
    print("Konfliktene får dominere. Prototypen blir forsinket og kvaliteten faller.")
    print("Flere i teamet mister motivasjonen og trekker seg tilbake.")

print("\nDine valg:")
print("1) ", "Regler i plenum" if valg1 == "a" else "Individuelle møter")
print("2) ", "Workshop etter skisser" if valg2 == "a" else "Fri flyt")
print("3) ", "Feire små seire" if valg3 == "a" else "Hardt leveransefokus")

print("\n--- Slutt på Vetle sin versjon ---\n")