# Altin.py / master.py
# Interaktiv historie – Erling som prosjektleder
# Del 2 av innleveringsoppgave 2 i IS-118.

# --- INTRODUKSJON ---
print("\n=== PROSJEKTLEDER ERLING ===")
print("Du er Erling. Teamet ditt krangler, og du må redde prosjektet.")
print("Du må ta 3 valg. Valgene dine får konsekvenser for sluttresultatet.")
print("-" * 30)

# --- VALG 1: SILJE OG SIVERT ---
print("\nSITUASJON 1: Konflikt om design og sikkerhet.")
print("Silje og Sivert krangler høylytt. Det har blitt personlig.")
print("A: Samle teamet til et dialogmøte (tar tid, men skaper forståelse).")
print("B: Ta en rask avstemning (effektivt, men kårer en 'taper').")

# Vi bruker en enkel løkke for å sikre at brukeren skriver a eller b
valg1 = ""
while valg1 not in ["a", "b"]:
    valg1 = input("Hva velger du (a/b)? ").strip().lower()

# Konsekvens av valg 1 (spilles av før neste konflikt)
if valg1 == "a":
    print("\n--> KONSEKVENS:")
    print("Du valgte dialog. Møtet tok lang tid, og dere har nå dårlig tid.")
    print("Men: Silje og Sivert forstår hverandre bedre, og luften er renset.")
else:
    print("\n--> KONSEKVENS:")
    print("Du valgte avstemning. Sivert vant 3-1.")
    print("Det gikk fort, men Silje ble sur, føler seg overkjørt og sier ingenting lenger.")

print("-" * 30)

# --- VALG 2: HAMDI OG JABIR ---
print("\nSITUASJON 2: Uenighet om digitale folkemøter.")
print("Hamdi og Jabir er uenige om løsningen. Konflikten ulmer.")
print("A: Gi dem et 24-timers 'miniprosjekt' sammen (rask tillit).")
print("B: Ta en grundig forhandling (tar tid, men gir varig løsning).")

valg2 = ""
while valg2 not in ["a", "b"]:
    valg2 = input("Hva velger du (a/b)? ").strip().lower()

# Konsekvens av valg 2
if valg2 == "a":
    print("\n--> KONSEKVENS:")
    print("Du valgte miniprosjektet. De jobbet intensivt sammen i 24 timer.")
    print("Det fungerte! De fikk en rask suksess og tonen er bedre.")
else:
    print("\n--> KONSEKVENS:")
    print("Du valgte forhandling. Det tok verdifull tid fra programmeringen.")
    print("Men: De fant en super løsning som ivaretar både sikkerhet og brukere.")

print("-" * 30)

# --- VALG 3: MOTIVASJON ---
print("\nSITUASJON 3: Teamet er slitne og stresset.")
print("Fristen nærmer seg. Hva gjør du for å få dem i mål?")
print("A: Ta en sosial samling/pause (bygge trivsel).")
print("B: Sette strenge delmål og styre tett (sikre fremdrift).")

valg3 = ""
while valg3 not in ["a", "b"]:
    valg3 = input("Hva velger du (a/b)? ").strip().lower()

# Konsekvens av valg 3
if valg3 == "a":
    print("\n--> KONSEKVENS:")
    print("Du valgte sosial samling. Folk fikk senket skuldrene.")
    print("Det ga ny energi, selv om dere mistet noen arbeidstimer.")
else:
    print("\n--> KONSEKVENS:")
    print("Du valgte strenge mål. Arbeidet går fremover fordi de må.")
    print("Men: Folk føler seg mikrostyrt og stemningen er dårlig.")

print("-" * 30)

# --- SLUTTRESULTAT ---
print("\n=== SLUTTRESULTAT ===")

# Sjekker kombinasjonen av valg for å gi riktig slutt (Endepunkt 1, 2 eller 3)

if valg1 == "a" and valg2 == "a" and valg3 == "a":
    # Dette er "drømmesenarioet" i rapporten (Endepunkt 1)
    print("RESULTAT: Suksess! (Endepunkt 1)")
    print("Du har gjenopprettet tilliten. Teamet leverer prototypen og samarbeider godt.")
    print("Du prioriterte relasjoner og dialog, og det lønte seg i lengden.")

elif valg1 == "b" and valg2 == "b"and valg3 == "b":
    # Hvis man overkjører folk (valg 1) og mikrostyrer (valg 3) går det galt (Endepunkt 3)
    print("RESULTAT: Krise! (Endepunkt 3)")
    print("Prosjektet mister samhold og blir forsinket.")
    print("Silje har meldt seg ut mentalt, og ingen er motiverte lenger.")
    print("De raske valgene dine ødela lagånden.")

else:
    # Alle andre kombinasjoner havner her (Endepunkt 2)
    print("RESULTAT: Helt greit. (Endepunkt 2)")
    print("Konfliktene er delvis løst, men relasjonene er fortsatt sårbare.")
    print("Dere leverer prototypen, men teamet er slitent og ikke helt sammensveiset.")
    print("\nTakk for at du spilte! Hvordan ville du håndtert situasjonene annerledes?")

