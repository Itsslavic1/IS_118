import time

# Lagrer valgkombinasjonen som bestemmer sluttresultatet
project_path = ""

# ---------------- INTRO ----------------
print("=" * 60)
print("VELKOMMEN TIL PROSJEKTSTORMEN")
print("=" * 60)

print("\nErling leder et tverrfaglig team som har gått inn i storming-fasen.")
print("Tre valg vil avgjøre teamets utvikling.\n")
time.sleep(1)


# ---------------- VALG 1 ----------------
print("-" * 50)
print("VALG 1: KONFLIKTEN MELLOM SILJE OG SIVERT")
print("-" * 50)
print("[A] Erling tar individuelle samtaler og roer konflikten.")
print("[B] Erling gjennomfører avstemning, men konflikten ulmer videre.\n")

valg_1 = ""
while valg_1 not in ['A', 'B']:
    valg_1 = input("Ditt valg (A/B): ").strip().upper()
    if valg_1 not in ['A', 'B']:
        print("Ugyldig valg. Prøv igjen.\n")

if valg_1 == "A":
    print("-> Du valgte dialog. Tonen roes ned og begge føler seg hørt.\n")
    project_path = "A"
else:
    print("-> Du valgte avstemning. Konflikten dempes ikke i dybden.\n")
    project_path = "B"

time.sleep(1)


# ---------------- VALG 2 ----------------
print("-" * 50)
print("VALG 2: HAMDI OG JABIR")
print("-" * 50)
print("[A] Erling gir dem et mini-prosjekt for å styrke samarbeidet.")
print("[B] Erling fasiliterer en vinn-vinn-dialog som avklarer behov.\n")

valg_2 = ""
while valg_2 not in ['A', 'B']:
    valg_2 = input("Ditt valg (A/B): ").strip().upper()
    if valg_2 not in ['A', 'B']:
        print("Ugyldig valg.\n")

if valg_2 == "A":
    print("-> Mini-prosjektet fungerer, men uenigheten løses ikke helt.\n")
    project_path += "A"
else:
    print("-> Vinn-vinn-dialogen gir god avklaring og bedre samarbeid.\n")
    project_path += "B"

time.sleep(1)


# ---------------- VALG 3 ----------------
print("-" * 50)
print("VALG 3: TEAMETS MOTIVASJON")
print("-" * 50)
print("[A] Erling arrangerer sosial samling for å styrke relasjoner.")
print("[B] Erling prioriterer planlegging med tydelige mål og frister.\n")

valg_3 = ""
while valg_3 not in ['A', 'B']:
    valg_3 = input("Ditt valg (A/B): ").strip().upper()
    if valg_3 not in ['A', 'B']:
        print("Ugyldig valg.\n")

if valg_3 == "A":
    print("-> Sosial samling gir bedre kommunikasjon og lavere stress.\n")
    project_path += "A"
else:
    print("-> Fremdriften øker, men presset blir høyere for flere.\n")
    project_path += "B"

time.sleep(1)


# ---------------- SLUTTRESULTAT ----------------
print("=" * 60)
print("SLUTTRESULTAT")
print("=" * 60)

# Gode samarbeid-kombinasjoner
gode_resultater = ["AAA", "AAB", "ABB"]
# Middels samarbeid-kombinasjoner
middels_resultater = ["BAA", "BAB", "BBA"]

if project_path in gode_resultater:
    print("\nRESULTAT 1: STERKT SAMARBEID")
    print("Teamet når norming-fasen. Tilliten er høy, og prosjektet leveres i tide.")

elif project_path in middels_resultater:
    print("\nRESULTAT 2: MIDLERTIDIG STABILITET")
    print("Teamet leverer, men relasjonene er fortsatt sårbare.")

else:
    print("\nRESULTAT 3: PROSJEKTET FORSINKES")
    print("Teamet mister samholdet, og konfliktene hemmer fremdriften.")

print("\nTakk for at du spilte!")
print("--- SLUTT ---")
