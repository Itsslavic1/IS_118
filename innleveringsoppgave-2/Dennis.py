import time
# Vi bruker 'time' for å lage pauser, så teksten ikke kommer alt på én gang.

# --- Variabel for å spore hele stien ----
project_path = "" 
# Dette er en tom tekststreng. Vi skal "lime" bokstaver på denne etter hvert som du tar valg.


# --- INTRODUKSJON ---
# HER ER FORKLARINGEN PÅ * TEGNET MED TEKST:
# Når man ganger en tekststreng ("=") med et tall (60), gjentar Python tegnet så mange ganger.
# "=" * 60 lager altså en lang linje med 60 er-lik-tegn: "==================..."
print("=" * 60)
print(" VELKOMMEN TIL PROSJEKTSTORMEN: ERLINGS VEIVALG")
print("=" * 60)

time.sleep(1) # Programmet venter i 1 sekund før det fortsetter
print("Du er Erling. Velg den beste veien for teamet.")
time.sleep(2)


# --- BESLUTNINGSPUNKT 1 ---
# Her lager vi en skilletrek med 50 bindestreker for å gjøre det ryddig i terminalen.
print("-" * 50) 
print("VALG 1: KONFLIKTEN MELLOM SILJE OG SIVERT")
print("-" * 50)
print("\n[A] DIALOG: Erling setter opp individuelle møter for å forstå Silje og Siverts ståsted. Målet er å dempe den personlige temperaturen før saken tas i plenum.")
print("[B] AVSTEMNING: Erling tvinger gjennom en rask avstemning over teknologivalget for å sikre fremdrift. Han unngår å snakke om de personlige relasjonene.")

valg_1 = ""

# While-løkken kjører så lenge valg_1 IKKE er 'A' og IKKE er 'B'.
# Dette tvinger brukeren til å skrive riktig før vi går videre.
while valg_1 not in ['A', 'B']:
    # input() henter det brukeren skriver.
    # .strip() fjerner mellomrom hvis brukeren kom borti space-tasten.
    # .upper() gjør om små bokstaver til store (f.eks. 'a' -> 'A').
    valg_1 = input("Ditt valg (A/B): ").strip().upper()
    
    if valg_1 not in ['A', 'B']:
        print("Ugyldig valg. Prøv igjen.")

# Her sjekker vi hva brukeren valgte
if valg_1 == 'A':
    print("-> Du valgte: DIALOG. Erling lykkes med å skille sak fra person. De får en felles forståelse av at de har samme mål, men ulike prioriteringer.")
    # HER ER FORKLARINGEN PÅ + TEGNET MED TEKST:
    # Vi setter variabelen lik "A".
    project_path = "A"
elif valg_1 == 'B':
    print("-> Du valgte: AVSTEMNING. Løsningen blir valgt, men konflikten ulmer videre i det skjulte. Sivert føler seg overkjørt og trekker seg unna diskusjoner.")
    project_path = "B"
    
# f-string (f"...") lar oss sette inn variabler direkte i teksten ved å bruke krøllparentes {}.
print(f"-> Din vei så langt: {project_path}")
time.sleep(2)


# --- BESLUTNINGSPUNKT 2 ---
print("\n" + "-" * 50) # \n betyr "ny linje" (enter-trykk), så vi får litt luft.
print("VALG 2: HAMDI OG JABIR'S DIALOG")
print("-" * 50)
print("\n[A] MINI-PROSJEKT: Erling gir Hamdi og Jabir en kort, felles oppgave de må løse raskt sammen. Målet er å bygge en liten suksess og gjenetablere tillit.")
print("[B] VINN-VINN FORHANDLING: Erling setter opp et formelt møte der han fasiliterer for å finne en felles løsning. Han fokuserer på de underliggende behovene deres.")

valg_2 = ""
while valg_2 not in ['A', 'B']:
    valg_2 = input("Ditt valg (A/B): ").strip().upper()
    if valg_2 not in ['A', 'B']:
        print("Ugyldig valg.")

if valg_2 == 'A':
    print("-> Du valgte: MINI-PROSJEKT. Oppgaven lykkes, og de to får en ny, positiv relasjon. Den originale uenigheten skyves likevel litt lenger frem i tid.")
    # TEKST-LIMING (Konkatenasjon):
    # Her tar vi det som allerede ligger i project_path (f.eks. "A") 
    # og limer på den nye bokstaven "A". Resultatet blir "AA".
    project_path = project_path + "A"
elif valg_2 == 'B':
    print("-> Du valgte: VINN-VINN. Begge parter føler seg hørt, og de finner en hybrid løsning som fungerer. Relasjonen er sterk, men prosessen var tidkrevende.")
    # Hvis project_path var "A", blir den nå "AB".
    project_path = project_path + "B"
    
print(f"-> Din vei så langt: {project_path}")
time.sleep(2)


# --- BESLUTNINGSPUNKT 3 ---
print("\n" + "-" * 50)
print("VALG 3: TEAMETS MOTIVASJON")
print("-" * 50)
print("\n[A] SOSIAL SAMLING: Erling setter av en halv dag til team-building utenfor kontoret. Han prioriterer å gjenoppbygge relasjoner og dempe stress.")
print("[B] TYDELIGE MÅL: Erling avlyser team-building og prioriterer en detaljert planleggingsøkt. Han setter knallharde deadlines for å holde fokus på leveransen.")

valg_3 = ""
while valg_3 not in ['A', 'B']:
    valg_3 = input("Ditt valg (A/B): ").strip().upper()
    if valg_3 not in ['A', 'B']:
        print("Ugyldig valg.")

if valg_3 == 'A':
    print("-> Du valgte: SOSIAL SAMLING. Teamet får senket skuldrene, og de sosiale båndene styrkes. Kommunikasjonen blir mer åpen og ærlig i ukene som følger.")
    # Limer på den siste bokstaven. Hvis vi hadde "AB", blir det nå "ABA".
    project_path = project_path + "A" 
elif valg_3 == 'B':
    print("-> Du valgte: TYDELIGE MÅL. Prosjektet får en boost i fremdrift, og alle vet hva de skal gjøre. Men mange føler seg utbrent og savner tillit til hverandre.")
    # Limer på den siste bokstaven.
    project_path = project_path + "B"
    
print(f"-> Din endelige vei: {project_path}")
time.sleep(3)


# --- KONKLUSJON ---
print("\n" + "=" * 60)
print(" SLUTT PÅ HISTORIEN")
print("=" * 60)

# Nå sjekker vi hele tekst-koden vi har bygget opp (f.eks "ABA").
# 'or' betyr at HVIS stien er AAA, ELLER stien er ABB... så får man dette resultatet.
if project_path == "AAA" or project_path == "ABB" or project_path == "AAB":
    print("\nRESULTAT 1: FANTASTISK SAMARBEID")
    print("Teamet har gjenopprettet tillit og er nå i 'norming'-fasen. Konfliktene ble løst gjennom dialog og relasjonsbygging.")
    print("UTFALL: Prosjektet leverer i tide med høy kvalitet og et godt arbeidsmiljø.")

# Sjekker middels gode kombinasjoner
elif project_path == "BAA" or project_path == "BAB" or project_path == "BBA":
    print("\nRESULTAT 2: MIDLERTIDIG STABILITET")
    print("Du prioriterte fremdrift i noen nøkkeløyeblikk, men klarte å redde relasjonene i andre. Tilliten er middels sterk.")
    print("UTFALL: Prosjektet leverer, men relasjonene er fortsatt sårbare og kan blusse opp igjen senere.")

# 'else' fanger opp alle andre kombinasjoner (de som er igjen).
else: 
    print("\nRESULTAT 3: PROSJEKTET FORSINKES")
    print("Fokus på raske avgjørelser og resultater førte til at teamet mistet samholdet. Kommunikasjonen er lav.")
    print("UTFALL: Prosjektet forsinkes på grunn av interne motstand og leveres med tvilsom kvalitet.")

print("\n--- SLUTT PÅ SPILLET ---")
